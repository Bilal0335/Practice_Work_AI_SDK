

# ! context_tool.py

from agents import function_tool,RunContextWrapper
# from my_data_type.context_data import userData
from my_data_type.context_data import UserData
import rich


# @function_tool
# async def fetch_user_age(ctx:RunContextWrapper[userData]):
#     """Age Function"""
#     rich.print(f"Context Tool::::::")
#     # rich.print(f"Context:::::: ",ctx)
#     # rich.print(f"Context:::::: ",ctx.context["name"])
#     rich.print(f"Context:::::: ",ctx.context.name)
#     # return f"Your age is {ctx.context['age']}."
#     return f"Your age is {ctx.context.age}."


@function_tool
async def fetch_user_age(ctx: RunContextWrapper[UserData]) -> str:
    """Return User's Age"""
    return str(f"{ctx.context.name}, your age is {ctx.context.age}.")


@function_tool
async def recommend_study_plan(ctx: RunContextWrapper[UserData]) -> str:
    """Recommend study/teaching plan based on role & age"""
    if ctx.context.role.lower() == "student":
        return str(f"{ctx.context.name}, since you are {ctx.context.age}, "
                   f"study {ctx.context.study_hours} hours daily. "
                   f"Focus on {ctx.context.favorite_subject}.")
    elif ctx.context.role.lower() == "teacher":
        return str(f"{ctx.context.name}, create engaging {ctx.context.favorite_subject} lessons for your class.")
    else:
        return str(f"{ctx.context.name}, motivate your child to study {ctx.context.study_hours} hours daily.")


@function_tool
async def motivate_user(ctx: RunContextWrapper[UserData]) -> str:
    """Give motivational message"""
    if ctx.context.role.lower() == "student":
        return str("Keep pushing, every effort counts toward your success!")
    elif ctx.context.role.lower() == "teacher":
        return str("Your guidance shapes the future of students.")
    else:
        return str("Your support is the best motivation for your child!")
