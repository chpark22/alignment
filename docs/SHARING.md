# Sharing CommsAlign

## Code review and edits

Repository: https://github.com/BroodrickVM/alignment

The owner can invite a reviewer in GitHub Settings → Collaborators → Add people,
using the reviewer's GitHub username or registered email. A private repository
requires access before cloning. The reviewer accepts the invitation, clones the
repository and follows the root README. Use a feature branch and pull request
for review before merging changes into main. An editor with write access can
change code; this does not give them permission to use private API credentials.

For public code, a fork and pull request is another option without write access.

## Browser-only dashboard access

A local 127.0.0.1 URL works on the machine running the app. For a class demo,
run Flask using the root README or open the forwarded port 8502 in a Codespace.
For a shareable deployment, use a Python WSGI host with Python 3.11,
`requirements.txt`, and the application entry point `commsalign:app`.

Review visibility and any course hosting requirements before deploying. Use
private reviewer access where appropriate. Share the actual URL provided after
successful deployment; no hosted URL has been verified at preparation time.
The requirements.txt in the repository root installs both tool dependencies.

Tool 2 and the Tool 1 sample review work without credentials. For live Tool 1,
add GW_AZURE_OPENAI_KEY, GW_ENDPOINT, GW_API_VERSION and GW_MODEL as private
environment variables. Optional GW_REASONING_EFFORT may also be set. Do not put
actual values in code, GitHub, screenshots or review messages. Do not activate
shared API credentials for unrestricted public use without deciding who may use
them and any associated usage costs.

## Reviewer checklist

Check survey scoring, tie behavior, suppression and incomplete data; read the
research access limits; test saving and exporting fictional discussion notes.
Tool 1 model quality requires separately configured GW access and live evaluation;
passing offline tests does not establish model quality. Do not add real employee
notes or copyrighted report extracts to GitHub.
