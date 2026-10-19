"""Empire G agent definition; original workshop examples are unchanged."""
import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

root_agent = Agent(
    name='empire_g_004_finisher',
    model=os.getenv("EMPIRE_G_MODEL", "gemini-flash-latest"),
    description='Selects one valuable near-complete asset and closes the remaining work to a defined finish.',
    instruction=(PROJECT_ROOT / "empire_g" / 'prompts/004_finisher.txt').read_text(
        encoding="utf-8"
    ),
    output_key='eg_004_finisher_result',
    tools=[],
)
