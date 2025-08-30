# ! runner_agent.py
from my_config.gemini_config import GEMINI_MODEL
from agents import Agent
from my_tool.math_tool import plus
import rich

# --- Math Assistant Agent ---
math_assistant = Agent(
    name="math_assistant",
    instructions="You are a helpful Math Teacher. Always use the 'plus' tool to calculate sums.",
    model=GEMINI_MODEL,
    tools=[plus]
)

# --- Main Runner Agent ---
runner_method_agent = Agent(
    name="runner_method_agent",
    instructions="""
        You are a helpful assistant.
        - You cannot answer math questions yourself.
        - Always hand off math problems to math_assistant.
    """,
    model=GEMINI_MODEL,
    handoffs=[math_assistant]  # Handoff ka agent
)
