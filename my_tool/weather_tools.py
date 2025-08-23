from agents import Runner, function_tool
from my_agent.weather_agent import weather_agent

@function_tool
async def get_weather() -> str:
    """Return today's weather"""
    return "It is sunny ☀️"

@function_tool
async def weather_agent_fun(query: str) -> str:
    """Use the weather agent to answer weather queries"""
    try:
        result = await Runner.run(
            weather_agent,
            query,
            max_turns=2,
            timeout=10,
        )
        return str(result.final_output).strip()
    except Exception as e:
        return f"[WeatherAgent error: {e}]"
