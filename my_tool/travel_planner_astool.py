

# ! travel_planner_astool.py
from agents import Agent
from rich.console import Console
from my_config.gemini_config import GEMINI_MODEL

console = Console()

# * ---------- Special Agents ----------

weather_agent = Agent(
    name="WeatherAgent",
    instructions="You give the current weather of the given city.",
    model=GEMINI_MODEL
)

flight_agent = Agent(
    name="FlightAgent",
    instructions="You suggest some flight timings for the given city.",
    model=GEMINI_MODEL
)

hotel_agent = Agent(
    name="HotelAgent",
    instructions="You recommend 2-3 hotels for the given city.",
    model=GEMINI_MODEL
)