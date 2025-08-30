
# ! dynamic_instruction.py
# from agents import RunContextWrapper,Agent
# from my_data_type.context_data import userData

# async def dynamic_instructions(ctx:RunContextWrapper[userData],agent:Agent[userData]):
#     # return f"User name is {ctx.context["name"]}, you are helpfull assistant."
#     return f"User name is {ctx.context.name}, you are helpfull assistant."

from agents import RunContextWrapper, Agent
from my_data_type.context_data import UserData

async def dynamic_instructions(ctx: RunContextWrapper[UserData], agent: Agent[UserData]):
    """
    Dynamic instructions for the agent.
    Ensure the model calls the correct tools.
    """
    base_rules = (
    "Use exactly one tool per question:\n"
    "- Age questions → fetch_user_age\n"
    "- Study hours, plan, schedule → recommend_study_plan\n"
    "- Motivation/encouragement → motivate_user\n"
    "Never call multiple tools. Never return null."
    )


    if ctx.context.role.lower() == "student":
        return (
            f"You are a Study Helper for {ctx.context.name}. "
            f"Guide them in {ctx.context.favorite_subject}. "
            f"{base_rules}"
        )
    elif ctx.context.role.lower() == "teacher":
        return (
            f"You are a Teaching Planner for {ctx.context.name}. "
            f"Help design {ctx.context.favorite_subject} lessons. "
            f"{base_rules}"
        )
    else:
        return (
            f"You are a Motivation Coach for {ctx.context.name}. "
            f"Encourage and support them. "
            f"{base_rules}"
        )
