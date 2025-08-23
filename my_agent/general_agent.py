from agents import Agent
from my_tool.weather_tools import weather_agent_fun
from my_config.groq_config import GROQ_MODEL
general_agent = Agent(
    name="GeneralAgent",
    instructions="Answer general purpose queries. Use tools when required.",
    tools=[weather_agent_fun],
    model=GROQ_MODEL
)
