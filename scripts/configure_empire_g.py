"""Configure the existing Gemini provider without exposing a key."""
from getpass import getpass
import json
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"


def read_setting(text, name):
    pattern = re.compile(r"^" + re.escape(name) + r"\s*=\s*(.*)$", re.MULTILINE)
    found = pattern.search(text)
    if not found:
        return ""
    return found.group(1).strip().strip('"').strip("'")


def replace_setting(text, name, value):
    replacement = name + "=" + json.dumps(value)
    pattern = re.compile(r"^" + re.escape(name) + r"\s*=.*$", re.MULTILINE)
    if pattern.search(text):
        return pattern.sub(lambda _: replacement, text)
    return text.rstrip() + "\n" + replacement + "\n"


def main():
    text = ENV_PATH.read_text(encoding="utf-8") if ENV_PATH.exists() else ""
    use_vertex = read_setting(text, "GOOGLE_GENAI_USE_VERTEXAI").lower()
    if use_vertex in ("true", "1"):
        raise SystemExit(
            "An existing Vertex AI configuration was found. It has been preserved. "
            "Configure this provider intentionally before using the Gemini API helper."
        )
    existing_key = read_setting(text, "GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
    prompt = "Google API key (hidden; Enter keeps the existing key): " if existing_key else "Google API key (hidden): "
    key = getpass(prompt).strip() or existing_key
    if not key:
        raise SystemExit("No key supplied. Configuration unchanged.")
    current_model = read_setting(text, "EMPIRE_G_MODEL") or os.getenv("EMPIRE_G_MODEL") or "gemini-flash-latest"
    model = input("Model [" + current_model + "]: ").strip() or current_model
    if any(c in key or c in model for c in ("\n", "\r")):
        raise SystemExit("Single-line values are required. Configuration unchanged.")
    text = replace_setting(text, "GOOGLE_GENAI_USE_VERTEXAI", "FALSE")
    text = replace_setting(text, "GOOGLE_API_KEY", key)
    text = replace_setting(text, "EMPIRE_G_MODEL", model)
    fd, temporary_name = tempfile.mkstemp(prefix=".empire-config-", dir=ROOT)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text.lstrip("\n"))
        temporary.chmod(0o600)
        temporary.replace(ENV_PATH)
    finally:
        temporary.unlink(missing_ok=True)
    print("Private configuration saved. No model request was made.")
    print("Next: python scripts/check_empire_g.py")


if __name__ == "__main__":
    main()
