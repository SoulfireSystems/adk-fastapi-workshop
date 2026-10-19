# Verification - Empire G starter setup

Date: October 19, 2026

User flow: select an Empire G agent in ADK Web, load its current prompt, supply project context, and request a response through the existing Gemini provider.

## Completed checks

| Check | Result | Evidence |
| --- | --- | --- |
| Class baseline preserved | Passed | Remote class-preserved-2026-10-19 points to fd5d2631f5bce42c863c9a08a3241d74412d0fe1. |
| Full clone | Passed | Local clone includes 89 reachable commits across the fetched branches. |
| Class source unchanged | Passed | All files tracked in the class baseline compare unchanged before the new-file-only commit. |
| Prompt inventory | Passed | All 18 unique IDs have nonempty prompt files and matching assignments. |
| ADK import/load | Passed | ADK 1.18.0 imports the Sales, Finisher and Chief of Staff definitions and loads their exact prompt files/output keys. |
| Dependency consistency | Passed | pip check: No broken requirements found. |
| Private configuration helper | Passed | Synthetic-key checks preserve unrelated settings, hide key output, create a private-mode file and preserve an existing Vertex AI configuration. |
| Ignore rules | Passed | .env and .venv/ are excluded by Git. |
| ADK server starts | Passed | Native ADK Web server starts with the specified agents directory. |
| Web assets served | Passed | GET / returns HTTP 200 and HTML. This is an HTTP smoke check, not a visual browser review. |
| Agent discovery | Passed | GET /list-apps returns HTTP 200 with all three new agents among 14 apps. |
| Live provider response | Not tested | No GOOGLE_API_KEY is configured in this task workspace. No model request was made. |
| External business tools | Not installed | The three definitions have empty tool lists. Work starts from the context supplied in their chat. |

The native server check used a short-lived loopback test server and shut it down afterward. The setup does not publish a production application, create a recurring task or enable inter-agent delegation.

## Next real check
Configure the existing provider privately using scripts/configure_empire_g.py, run scripts/check_empire_g.py, open ADK Web and send the first Chief of Staff assignment from START_EMPIRE_G.md. A live response depends on a valid available model and account access.

Use the per-agent acceptance cases for behavioral evaluation after that first live connection. Offline definition loading does not establish output quality.
