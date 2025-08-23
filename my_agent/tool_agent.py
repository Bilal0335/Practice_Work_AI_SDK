
# ! tool_agent.py

from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tool.math_tool import plus, subtract, multiply
from rich import print
from my_data_type.math_data import SimpleResult
from my_tool.weather_tool import fetch_weather

# Create the tools agent
tools_agent = Agent(
    name='tools_agent',
    instructions="You can perform math operations and fetch weather.",
    model=GEMINI_MODEL,
    tools=[plus, subtract, multiply,fetch_weather],
    output_type=SimpleResult
)

# *Debug info (to check agent is loaded correctly)

# print("[bold green]=== Agent Name ===[/bold green]", tools_agent.name)
# print("[bold cyan]=== Agent Tools ===[/bold cyan]", [t.name for t in tools_agent.tools])
# print("[bold yellow]=== Agent Tools ===[/bold yellow]", tools_agent.tools)
