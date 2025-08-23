

# ! weather_tool.py
from agents import function_tool
from my_data_type.weather_data import Location

# ---- Weather Tool ----
@function_tool
async def fetch_weather(location: Location) -> str:
    """Fetch the weather for a given location."""
    print("[cyan]=== Tool Used: FETCH WEATHER ===[/cyan]")
    # Fake weather response for practice
    return "sunny"