const reviewForm = document.querySelector("[data-review]");
const reviewTarget = document.querySelector("[data-review-error], [data-review-complete]");
reviewTarget?.focus();
const staleReview = document.querySelector("[data-review-stale]");
reviewForm?.addEventListener("input", event => {
  if (staleReview && ["kind", "draft"].includes(event.target.name)) staleReview.hidden = false;
  if (event.target.name === "kind") {
    for (const rubric of document.querySelectorAll("[data-rubric]")) {
      rubric.hidden = rubric.dataset.rubric !== event.target.value;
    }
  }
});
reviewForm?.addEventListener("submit", () => {
  const button = reviewForm.querySelector("button[type=submit]");
  button.disabled = true;
  button.textContent = "Reviewing draft…";
});
window.addEventListener("pageshow", () => {
  const button = reviewForm?.querySelector("button[type=submit]");
  if (button) {
    button.disabled = false;
    button.textContent = "Evaluate draft";
  }
});

function download(data, type, filename) {
  const url = URL.createObjectURL(new Blob([data], {type}));
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
document.querySelector("[data-download-review]")?.addEventListener("click", () => {
  download(document.querySelector("#review-data").textContent, "application/json", "commsalign-message-review.json");
});
document.querySelector("[data-download-revision]")?.addEventListener("click", () => {
  download(document.querySelector("#revision").value, "text/plain", "commsalign-revised-draft.txt");
});

const period = document.querySelector("#period");
document.querySelector("#team")?.addEventListener("change", event => {
  if (period) period.disabled = period.dataset.team !== event.target.value;
});

const blocked = document.querySelector("#blocked-groups");
const notes = document.querySelector("[data-notes]");
const prefix = "commsalign:notes:";
if (blocked) {
  const groups = JSON.parse(blocked.textContent);
  try {
    for (const key of Object.keys(sessionStorage)) {
      if (!key.startsWith(prefix)) continue;
      const [team, period] = JSON.parse(key.slice(prefix.length));
      if (groups.some(group => group[0] === team && group[1] === period)) {
        sessionStorage.removeItem(key);
      }
    }
  } catch {
    // Browser storage can be unavailable in private or embedded contexts.
  }
}
if (notes) {
  const key = prefix + JSON.stringify(JSON.parse(notes.dataset.context));
  const status = notes.querySelector("[data-note-status]");
  let saved = {};
  try {
    saved = JSON.parse(sessionStorage.getItem(key) || "{}");
  } catch {
    status.textContent = "Browser storage is unavailable. Notes can still be exported.";
  }
  const restore = () => {
    notes.reset();
    for (const [name, value] of Object.entries(saved)) {
      const field = notes.elements.namedItem(name);
      if (field) field.value = value;
    }
  };
  restore();
  notes.querySelector("[data-save]").addEventListener("click", () => {
    saved = Object.fromEntries(new FormData(notes));
    try {
      sessionStorage.setItem(key, JSON.stringify(saved));
      status.textContent = "Notes saved in this tab.";
    } catch {
      status.textContent = "Notes saved on this page. Export them before leaving.";
    }
  });
  notes.querySelector("[data-clear]").addEventListener("click", () => {
    try {
      sessionStorage.removeItem(key);
      saved = {};
      restore();
      status.textContent = "Saved notes cleared.";
    } catch {
      status.textContent = "Browser storage could not be cleared.";
    }
  });
  notes.addEventListener("formdata", event => {
    for (const field of notes.querySelectorAll("[name]")) {
      event.formData.set(field.name, saved[field.name] ?? field.defaultValue ?? field.options?.[0]?.value ?? "");
    }
  });
}
