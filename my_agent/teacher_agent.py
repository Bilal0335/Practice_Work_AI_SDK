
# ! teacher_agent.py
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL
from my_config.openrouter_config import OPENROUTER_MODEL
from agents import Agent


gemini_agent = Agent(
    name="gemini_agent",
    instructions="Your are helpfull teacher_agent.",
    model=GEMINI_MODEL,
)

groq_agent = Agent(
    name="groq_agent",
    instructions="Your are helpfull groq_agent.",
    model=GROQ_MODEL,
)

openrouter_agent = Agent(
    name="openrouter_agent",
    instructions="Your are helpfull openrouter_agent.",
    model=OPENROUTER_MODEL,
)


# ! Agent Level → har agent ka apna provider/model fix kar dena