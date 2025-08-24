
# ! dynamic_instruction.py
from agents import RunContextWrapper,Agent
from my_data_type.context_data import userData

async def dynamic_instructions(ctx:RunContextWrapper[userData],agent:Agent[userData]):
    # return f"User name is {ctx.context["name"]}, you are helpfull assistant."
    return f"User name is {ctx.context.name}, you are helpfull assistant."