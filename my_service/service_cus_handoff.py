

# ! service_cus_handoff.py
from agents import RunContextWrapper
from my_data_type.custom_handoff_data import MathReasoning
import rich


async def service(ctx:RunContextWrapper,input_data:MathReasoning):
    rich.print(ctx.context)
    rich.print(input_data.reasoning)
    rich.print(input_data.result)


# async def service(ctx:RunContextWrapper):
#     rich.print(ctx.context)