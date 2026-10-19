"""Empire G agent definition; original workshop examples are unchanged."""
import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

root_agent = Agent(
    name='empire_g_001_sales',
    model=os.getenv("EMPIRE_G_MODEL", "gemini-flash-latest"),
    description='Turns qualified inquiries into tailored offers, proposals and a verifiable next sales action.',
    instruction=(PROJECT_ROOT / "empire_g" / 'prompts/001_sales.txt').read_text(
        encoding="utf-8"
    ),
    output_key='eg_001_sales_result',
    tools=[],
)
