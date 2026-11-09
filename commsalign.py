"""Flask entry point for the CommsAlign worksheet."""

from dataclasses import asdict
from io import BytesIO
from pathlib import Path

from flask import Flask, abort, render_template, request, send_file

from app.organizational.analyzer import analyze_csv
from app.organizational.evidence_validation import load_evidence_validation_matrix
from app.organizational.report import ITEM_TOPICS, item_tie_notice, render_report
from app.organizational.workflow import DECISIONS, OUTCOMES, discussion_summary
from app.tool1.judge import check_and_label
from app.tool1.pipeline import rescore, run
from app.tool1.rubrics import RUBRICS

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 128 * 1024
SAMPLE = Path(__file__).resolve().parent / "data/organizational/sample_q12_results.csv"
EXAMPLE = "Please send the revised onboarding checklist by Friday. Use last month’s template and flag any steps that need an owner."


def attachment(text, filename, mimetype="text/plain"):
    response = send_file(BytesIO(text.encode("utf-8")), mimetype=mimetype,
                         as_attachment=True, download_name=filename, max_age=0)
    response.headers["Cache-Control"] = "no-store"
    return response


@app.after_request
def protect_review_content(response):
    if request.endpoint in {"coach", "diagnostic"}:
        response.headers["Cache-Control"] = "no-store"
    return response


@app.get("/")
def overview():
    return render_template("overview.html", page="overview")


@app.route("/message-coach", methods=["GET", "POST"])
def coach():
    kind = request.form.get("kind", "task_instruction")
    draft = request.form.get("draft", "")
    example = request.args.get("example") == "1" and request.method == "GET"
    result = rewrite = after = error = None
    revised = request.form.get("operation") == "rescore"
    if example:
        draft = EXAMPLE
        rubric = RUBRICS[kind]
        evidence = [
            ("send the revised onboarding checklist", 4, "The requested deliverable is clear."),
            ("by Friday", 4, "A deadline is stated."),
            ("", None, "The draft does not explain why the checklist is being revised."),
            ("Use last month’s template", 4, "The draft points the recipient to a template."),
            ("flag any steps that need an owner", 3, "The draft asks for flagged items but gives no intermediate check-in."),
        ]
        result = check_and_label(rubric, draft, {
            "rubric_id": rubric.rubric_id,
            "confidence": {"level": "medium", "note": "Illustrative review prepared for the demo."},
            "scores": {
                key: {"status": "scored" if score is not None else "not_assessable",
                      "score": score, "note": note, "evidence": [quote] if quote else []}
                for key, (quote, score, note) in zip(rubric.dimensions, evidence)
            },
        })
    elif request.method == "POST":
        if kind not in RUBRICS:
            error = "Choose a supported message type."
            kind = "task_instruction"
        elif not draft.strip() or len(draft) > 12000:
            error = "Enter a draft between 1 and 12,000 characters."
        elif request.form.get("consent") != "yes":
            error = "Confirm consent before sending the draft for review."
        else:
            from app.tool1.config import load_settings
            try:
                load_settings()
            except RuntimeError:
                error = "GW Azure is not configured. Use the sample review to try the workflow."
            if not error:
                try:
                    if revised:
                        result = rescore(draft, kind)
                    else:
                        pipeline = run(draft, kind)
                        result, rewrite, after = pipeline.before, pipeline.rewrite, pipeline.after
                except Exception:
                    error = "The review could not be completed. Check your GW Azure configuration or try again."
    review = None
    if result:
        review = {"draft": draft, "kind": kind, "result": asdict(result),
                  "rewrite": asdict(rewrite) if rewrite else None,
                  "after": asdict(after) if after else None, "example": example}
    return render_template("coach.html", page="coach", kind=kind, draft=draft,
                           rubrics=RUBRICS, result=result, error=error, example=example,
                           review=review, rewrite=rewrite, after=after, revised=revised,
                           cards={card.id: card for card in rewrite.cards} if rewrite else {})


@app.route("/team-diagnostic", methods=["GET", "POST"])
def diagnostic():
    threshold = request.values.get("minimum", 5, type=int)
    if not 1 <= threshold <= 10000:
        abort(400)
    reports = analyze_csv(SAMPLE, minimum_responses=threshold)
    team = request.values.get("team", reports[0].team_id)
    team_reports = [r for r in reports if r.team_id == team]
    if not team_reports:
        abort(404)
    period = request.values.get("period", team_reports[0].period or "")
    report = next((r for r in team_reports if (r.period or "") == period), None)
    if report is None:
        if request.method == "POST" or request.args.get("download"):
            abort(404)
        report = team_reports[0]
    matrix = load_evidence_validation_matrix()
    signals = report.communication_signals if not report.suppressed else ()
    selected = request.values.get("item", signals[0].source_q12_item if signals else "")
    signal = next((s for s in signals if s.source_q12_item == selected), None)
    if request.args.get("download") == "diagnostic":
        if report.suppressed:
            abort(403)
        return attachment("Synthetic demonstration data.\n\n" + render_report(report),
                          "commsalign-diagnostic-summary.txt")
    if request.method == "POST":
        if signal is None:
            abort(403)
        notes = {key: request.form.get(key, "").strip()[:3000]
                 for key in ("observations", "reflection", "action", "owner", "follow_up")}
        outcome = request.form.get("outcome")
        decision = request.form.get("decision")
        if outcome not in OUTCOMES or decision not in DECISIONS:
            abort(400)
        notes.update(outcome=outcome, decision=decision)
        return attachment(discussion_summary(report, selected, matrix.get_by_source_item(selected), notes),
                          "commsalign-discussion-summary.txt")
    return render_template(
        "diagnostic.html", page="diagnostic", reports=reports, team_reports=team_reports,
        report=report, signals=signals, signal=signal, matrix=matrix, topics=ITEM_TOPICS,
        tie_notice=item_tie_notice(report) if not report.suppressed else "",
        outcomes=OUTCOMES, decisions=DECISIONS,
        blocked=[[r.team_id, r.period or ""] for r in reports if r.suppressed],
    )
