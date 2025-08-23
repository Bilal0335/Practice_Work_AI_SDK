

from agents import function_tool

@function_tool(name_override="plan_trip")
def get_travel_plan(city: str) -> str:
    """Plan Travel for your city"""
    return f"Travel Plan for {city} is not available"