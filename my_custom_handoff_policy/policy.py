

# ! policy.py
from agents import RunContextWrapper

async def en(ctx:RunContextWrapper,agent):
    if ctx.context["age"]>=18:
        return True
    else:
        return False