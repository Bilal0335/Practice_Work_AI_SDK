
# ! guardrails_agent.py

from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_data_type.output_data_guardrails import MyOutputGuardrail

guardrail_agent = Agent(
    name="Guardrail Checker",
    instructions="check  Hotel Sannata's queries and account or tax query.",
    model=GEMINI_MODEL,
    output_type=MyOutputGuardrail
)
