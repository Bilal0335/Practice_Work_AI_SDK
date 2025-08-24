

# ! context_tool.py

from agents import function_tool,RunContextWrapper
from my_data_type.context_data import userData
import rich


@function_tool
async def fetch_user_age(ctx:RunContextWrapper[userData]):
    """Age Function"""
    rich.print(f"Context Tool::::::")
    # rich.print(f"Context:::::: ",ctx)
    # rich.print(f"Context:::::: ",ctx.context["name"])
    rich.print(f"Context:::::: ",ctx.context.name)
    # return f"Your age is {ctx.context['age']}."
    return f"Your age is {ctx.context.age}."
