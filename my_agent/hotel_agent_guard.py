


from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_guardrails_function.guardrails_input_fun import guardrail_input_fun
from my_guardrails_function.guardrails_output_fun import guardrail_output_fun

hotel_agent_guardrail = Agent(
    name="Hotel Customer Care Assistant",
    instructions="""You are a helpful Hotel Sannata's Customer Care assistant, Your name is Atma Ram.
- Hotel Sannata owner name is Mr. Ratan Lal.
- Hotel Sannata total rooms 200.
- 20 rooms not available for public (special guest only).
""",
    model=GEMINI_MODEL,
    input_guardrails=[guardrail_input_fun],
    output_guardrails=[guardrail_output_fun]
)
