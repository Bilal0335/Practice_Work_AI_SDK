


# ! output_agent.py

from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_data_type.output_data import NameCheck


output_type_agent = Agent(
    name='output_type_agent',
    instructions="Your are helpfull assistant.",
    model=GEMINI_MODEL,
    output_type=NameCheck
)


