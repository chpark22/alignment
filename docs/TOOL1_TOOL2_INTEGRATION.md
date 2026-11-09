# Shared AlignAgent interface

Install the root `requirements.txt` and start the Flask application as
described in the README.

Overview, Message Coach and Team Diagnostic share the top navigation.
The Flask routes reuse the existing rubric, analysis, and evidence modules.

Tool 1 uses the same teammates' source snapshot as the previous local merge;
see app/tool1/UPSTREAM.md. The source version has not been confirmed by teammates.
Its judge and label rules are preserved. The rewriter and automatic cross-tool
handoff are not implemented. The existing local personal-agent CLI is separate.

For live evaluation, copy .env.example to .env and configure GW_AZURE_OPENAI_KEY,
GW_ENDPOINT, GW_API_VERSION and GW_MODEL from the GW guide. Never commit secrets.
Only explicit draft submission with consent calls the model. Results are kept
in session state and can be explicitly downloaded or cleared. No live model
request is included in integration verification; mocked tests are not a claim
that the GW connection is operational.

This restored merge is local; it has not been pushed or deployed publicly.
