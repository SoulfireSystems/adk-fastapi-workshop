# Start Empire G without losing the class

## What has been preserved
Your instructor's repository was already forked into SoulfireSystems/adk-fastapi-workshop. The class examples, documents and original branch history remain available.

- Original class: https://github.com/SoulfireSystems/adk-fastapi-workshop/tree/main
- Preserved class snapshot: https://github.com/SoulfireSystems/adk-fastapi-workshop/tree/class-preserved-2026-10-19
- Empire G working branch: https://github.com/SoulfireSystems/adk-fastapi-workshop/tree/empire-g-build
- Snapshot commit: fd5d2631f5bce42c863c9a08a3241d74412d0fe1

The preserved snapshot is another branch pointing to the class commit. It is not a GitHub branch-protection rule or a separate repository. Build on empire-g-build. Leave main and the preserved branch as your classroom references.

A full local clone includes the repository history and remote branches. The working clone made during this task is in this ChatGPT workspace; it does not automatically create a folder on your own computer.

## What was found before this setup
The repo had the instructor's nine step examples, sequential/parallel examples and the branches initialCourseEnvironment, feature/project-management-agent and contentDistribution. The inspected history is instructor-authored. No installed Chief of Staff, Sales or Finisher agent definitions were found in that history.

The previous 18-agent pack supplied prompts, assignments and an implementation brief. This branch now adds the prompt files plus real ADK definitions for 001 Sales, 004 Finisher and 012 Chief of Staff. The other 15 remain prompt files to activate later. None of these definitions connects your email, payments, calendar or private files.

## 1. Open the correct branch
Open the Empire G working-branch link above. Near the top of GitHub, the branch selector should read empire-g-build.

Click empire_g, then prompts. That is where your 18 instruction files live.
Click adk_agents, then empire_g_012_chief_of_staff, then agent.py. That small Python file loads your Chief of Staff prompt into an ADK Agent.

To return to the class, switch the branch selector to main or class-preserved-2026-10-19. Do not merge the build into the preserved branch.

## 2. Clone the working copy onto your computer or into your coding workspace
Use a terminal in the folder where you keep projects:

```bash
git clone --branch empire-g-build https://github.com/SoulfireSystems/adk-fastapi-workshop.git Empire-G-Agents
cd Empire-G-Agents
```

If you are using the class's browser coding workspace, open its terminal and use the same commands in a NEW project folder. Do not delete the original classroom folder. GitHub's website stores and edits code; opening an agent.py page does not run the agent.

The clone command copies the Git history as well as the files. GitHub Code > Download ZIP provides the selected branch's files but not its Git history.

## 3. Install the small Empire G runtime
Python 3.10+ is required. Use a separate virtual environment so this setup does not change the class's existing environment.

Mac, Linux or the class's Linux browser terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-empire-g.txt
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-empire-g.txt
```

This setup pins google-adk 1.18.0 to match the workshop generation. It is a reproducible starting point, not a claim that this is the latest ADK version. A future upgrade belongs on the working branch after testing.

## 4. Configure model access privately
This first version uses the Google Gemini provider already used by the class. Use your existing Google API access if available. Manage keys in Google AI Studio: https://aistudio.google.com/apikey . Do not paste keys into chat or a committed GitHub file.

Run:

```bash
python scripts/configure_empire_g.py
```

The helper asks for the key with hidden input, asks which model to use and writes the ignored .env file. It preserves unrelated settings and prints no key. The default model alias is gemini-flash-latest; choose an available model for your account if needed. The helper does not verify account quota, enable billing or call a model.

The repository's .gitignore excludes .env. Your normal local setup should keep it private.

## 5. Check the setup
```bash
python scripts/check_empire_g.py
```

The check validates all 18 prompt files and loads the three ADK definitions. It reports whether a key is configured without printing its value. It makes no model request.

## 6. Open the agent screen
```bash
adk web adk_agents --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000 on the machine running the command. In a browser coding workspace, use its forwarded port-8000 preview.

This uses ADK's actual runtime instead of the workshop's custom chat backend. Treat it as your local development screen, not a public production application.

Choose empire_g_012_chief_of_staff in the agent selector. Paste this first assignment and the current project notes it should work from:

> Use the project notes I supply below. Identify one near-term buyer action, one delivery obligation and one asset to finish. Give each a concrete output and finish line. Prepare what you can now. Mark missing facts clearly. Do not invent account access, cash balances or completed work. End with my Top 3 and one decision.

Then paste a short current-state note. It can be as simple as three project names, what exists and what is blocked. The agent cannot see your ChatGPT conversations automatically.

A live response uses your configured model/provider access. Setup checks do not establish that account access or billing quota is available.

## 7. Use Sales and Finisher
Switch to empire_g_001_sales for proposals and buyer follow-ups. Its starter assignment is empire_g/assignments/001_sales.md.

Switch to empire_g_004_finisher to complete one asset. Its starter assignment is empire_g/assignments/004_finisher.md.

These are separate agent sessions in this first version. Copy an explicit handoff between them when needed. Automated inter-agent delegation is a later step.

## 8. Change the behavior without editing the class
Edit the corresponding file in empire_g/prompts/. Save, restart ADK Web and start a fresh session. The agent.py file loads that prompt at import time.

Use the matching acceptance case in empire_g/assignments/ to test the change. Save your work only on empire-g-build:

```bash
git status --short --branch
git add empire_g adk_agents/empire_g_001_sales adk_agents/empire_g_004_finisher adk_agents/empire_g_012_chief_of_staff scripts START_EMPIRE_G.md requirements-empire-g.txt
git commit -m "Update Empire G agents"
git push origin empire-g-build
```

Do not add .env, client records or private drafts. The first-stage agents can work from information pasted into their local chat; business integrations have not been installed.

## Where the parts live
| Part | Path |
| --- | --- |
| All 18 prompts | empire_g/prompts/ |
| First assignments and acceptance cases | empire_g/assignments/ |
| Role inventory | empire_g/agent_manifest.json |
| Sales definition | adk_agents/empire_g_001_sales/agent.py |
| Finisher definition | adk_agents/empire_g_004_finisher/agent.py |
| Chief of Staff definition | adk_agents/empire_g_012_chief_of_staff/agent.py |
| Private configuration helper | scripts/configure_empire_g.py |
| Offline check | scripts/check_empire_g.py |

## Source references
Google ADK Python quickstart: https://google.github.io/adk-docs/get-started/python/
Google ADK source at the pinned version: https://github.com/google/adk-python/tree/v1.18.0
Repository source and local inspection: October 19, 2026.

Read empire_g/VERIFICATION.md for the checks actually completed. Definitions loading is distinct from a tested live model response.
