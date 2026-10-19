"""Empire G agent definition; original workshop examples are unchanged."""
import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

root_agent = Agent(
    name='empire_g_012_chief_of_staff',
    model=os.getenv("EMPIRE_G_MODEL", "gemini-flash-latest"),
    description='Coordinates the Empire G portfolio, priorities, agent handoffs and decision queue.',
    instruction=(PROJECT_ROOT / "empire_g" / 'prompts/012_chief_of_staff.txt').read_text(
        encoding="utf-8"
    ),
    output_key='eg_012_chief_of_staff_result',
    tools=[],
)
