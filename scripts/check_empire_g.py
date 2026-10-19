"""Offline prompt/ADK loading check. Does not call an AI provider."""
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "adk_agents"))
manifest = json.loads((ROOT / "empire_g" / "agent_manifest.json").read_text())
expected_ids = [f"{n:03d}" for n in range(1, 19)]
actual_ids = sorted(item["id"] for item in manifest["agents"])
if actual_ids != expected_ids:
    raise SystemExit("The prompt inventory is incomplete or has duplicate IDs.")

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
    version = importlib.metadata.version("google-adk")
except (ImportError, importlib.metadata.PackageNotFoundError):
    raise SystemExit("Install requirements-empire-g.txt in your virtual environment first.")

print("ADK version:", version)
loaded = []
for item in manifest["agents"]:
    prompt = ROOT / "empire_g" / item["instruction_file"]
    assignment = ROOT / "empire_g" / item["assignment_file"]
    if not prompt.is_file() or not prompt.read_text(encoding="utf-8").strip():
        raise SystemExit("Missing prompt for agent " + item["id"])
    if not assignment.is_file():
        raise SystemExit("Missing assignment for agent " + item["id"])
    if item.get("definition_added"):
        module = importlib.import_module(item["adk_name"] + ".agent")
        agent = module.root_agent
        if agent.name != item["adk_name"] or agent.output_key != item["suggested_output_key"]:
            raise SystemExit("Agent identity/output key mismatch: " + item["id"])
        if agent.instruction != prompt.read_text(encoding="utf-8"):
            raise SystemExit("Prompt loading mismatch: " + item["id"])
        loaded.append(item["adk_name"])
print("Prompt inventory: all 18 present.")
print("Loaded ADK definitions:", ", ".join(loaded))
print("GOOGLE_API_KEY:", "configured" if bool(os.getenv("GOOGLE_API_KEY")) else "not configured")
print("Model setting:", os.getenv("EMPIRE_G_MODEL", "gemini-flash-latest"))
print("No model call, email, payment or account connection was performed.")
