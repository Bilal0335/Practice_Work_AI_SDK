from agents import Agent
from my_tool.proofread_tool import proofread_text
from my_config.groq_config import GROQ_MODEL
teacher_agent = Agent(
    name="Teacher",
    instructions="Help students write clearly. Use tools when asked to fix text.",
    tools=[proofread_text],
    model=GROQ_MODEL
)
