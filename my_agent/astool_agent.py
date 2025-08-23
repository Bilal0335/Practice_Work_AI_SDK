
# ! astool_agent.py
# import rich
# from my_config.gemini_config import GEMINI_MODEL
# from agents import Agent
# from my_tool.math_tool import plus,subtract,multiply


# first_agent = Agent(
#     name="first_agent",
#     instructions="Your are helpfull teacher_agent.",
#     model=GEMINI_MODEL,
#     tools=[plus,subtract,multiply]
# )



# sec_agent = Agent(
#     name="sec_agent",
#     instructions="Your are helpfull assistant.",
#     model=GEMINI_MODEL,
#     tools=[first_agent.as_tool(
#         tool_name="teacher_agent",
#         tool_description="Thius is a teacher_agent."
#     )]
# )

# rich.print(sec_agent.tools)


# ! Travel Planner (as Tool)
from my_tool.travel_planner_astool import weather_agent,flight_agent,hotel_agent
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL

# * ----------- Orchestrator Agent -----------

orchestrator_agent = Agent(
    name="OrchestratorAgent",
    instructions=(
        "You are a travel planner. "
        "When the user asks for a trip, you first call the weather tool, "
        "then the hotel tool, and finally the flight tool to provide a full plan."
    ),
    model=GEMINI_MODEL,
    tools=[
        weather_agent.as_tool(
            tool_name="get_weather",
            tool_description="Get the current weather of a city."
        ),
        hotel_agent.as_tool(
            tool_name="get_hotels",
            tool_description="Suggest hotels for a city."
        ),
        flight_agent.as_tool(
            tool_name="get_flights",
            tool_description="Suggest flight timings for a city."
        ),
    ],
)
