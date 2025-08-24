from my_config.groq_config import GROQ_MODEL
from agents import Agent
from my_tool.context_tool import fetch_user_age
from instruction.dynamic_instruction import dynamic_instructions
from my_data_type.context_data import userData


context_agents: Agent = Agent[userData](
    name="context_agents",
    # instructions=(
    #     "You are a helpful assistant. "
    #     "If the user asks about their age, always use the fetch_user_age tool. "
    #     "Do not answer age questions without calling the tool."
    # ),
    instructions=dynamic_instructions,
    model=GROQ_MODEL,
    tools=[fetch_user_age]
)
