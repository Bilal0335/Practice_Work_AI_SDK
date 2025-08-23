from agents import Agent
from my_tool.weather_tools import get_weather
from my_config.groq_config import GROQ_MODEL
weather_agent = Agent(
    name="WeatherChecker",
    instructions="Use available tools to answer weather questions clearly.",
    tools=[get_weather],
    model=GROQ_MODEL
)
