
# custom_fun_agent.py
from agents import Agent
from my_config.groq_config import GROQ_MODEL
from my_config.gemini_config import GEMINI_MODEL
from my_tool.custom_fun_tool import substracts
from agents.agent import StopAtTools

# cust_fun_agents = Agent(
#     name="assistant",
#     instructions="This is a helpfll assistant",
#     # tools=[substracts,plus],
#     tools=[substracts,plus],
#     model=GROQ_MODEL
#     # model=GEMINI_MODEL
# )

# print(cust_fun_agents.tools)

# for s in cust_fun_agents.tools:
#     print(s.params_json_schema)

# cust_fun_agents = Agent(
#     name="assistant",
#     instructions=(
#         "You are a helpful assistant. "
#         "👉 If the user asks to add numbers or talks about addition, use the 'plus' tool. "
#         "👉 If the user does not ask about addition, then just reply normally without calling any tool."
#     ),
#     tools=[plus],
#     model=GROQ_MODEL,
#     tool_use_behavior=StopAtTools(stop_at_tool_names=["plus"])
# )

# cust_fun_agents = Agent(
#     name="assistant",
#     instructions=(
#     "You are a helpful assistant. "
#     "👉 If the user asks to add numbers or talks about addition, use the 'plus' tool. "
#     "👉 If the user asks to subtract numbers, use the 'substracts' tool. "
#     "👉 Otherwise, just reply normally without calling any tool."
#     ),
#     tools=[substracts,plus],
#     # tool_use_behavior=StopAtTools(stop_at_tool_names=["plus", "substracts"]),
#     model=GROQ_MODEL
# )


cust_fun_agents = Agent(
    name="assistant",
    instructions=(
        "You are a helpful assistant. "
        "👉 If the user asks to subtract numbers, use the 'substracts' tool. "
        "👉 Otherwise, just reply normally without calling any tool."
    ),
    tools=[substracts],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["plus", "substracts"]),
    model=GROQ_MODEL
)


