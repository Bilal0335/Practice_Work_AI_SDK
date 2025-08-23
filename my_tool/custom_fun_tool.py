
# ! custom_fun_tool.py
from agents import FunctionTool,RunContextWrapper,function_tool
import rich
from validators.valid_tool import tool_validate
from my_data_type.math_data import ToolMyScehma
from rich import print


# async def substracts_fun(ctx:RunContextWrapper,arg:str):
#     print("\n[green]=== Tool Used: Substract ===[/green]")
#     obj = ToolMyScehma.model_validate_json(arg)
#     res = obj.n1 - obj.n2
#     return f"your answer is {res}"
    
# ! Agar FunctionTool manually banate ho error handling
async def substracts_fun(ctx: RunContextWrapper, arg: str):
    try:
        obj = ToolMyScehma.model_validate_json(arg)

        # 🚨 Error check (jaise plus me tha)
        if obj.n1 < 0 or obj.n2 < 0:
            raise ValueError("Negative numbers not allowed in subtraction.")

        res = obj.n1 - obj.n2
        return f"✅ Your answer is {res}"
    except Exception as e:
        print(f"[red]Substract Tool Error:[/red] {str(e)}")
        return f"❌ Sorry, subtraction tool failed: {str(e)}"

substracts = FunctionTool(
    name="substracts",
    description="substracts function",
    params_json_schema=ToolMyScehma.model_json_schema(),
    on_invoke_tool=substracts_fun,
    is_enabled=True #by ndefaul true hota hy active
    # is_enabled=False #deactive
    # is_enabled=tool_validate
)



# @function_tool(name_override="plus_function",description_override="this is a function override",is_enabled=tool_validate)
# async def plus(n1: int, n2: int) -> str:
#     """This is a Plus Function.
    
#     Args:
#         n1 (int): First number
#         n2 (int): Second number
        
#     Returns:
#         str: The sum in string format
#     """
#     print("[green]=== Tool Used: PLUS ===[/green]")
#     return f"your sum is {n1 + n2}"



# def my_custom_error_function(ctx: RunContextWrapper, error: Exception) -> str:
#     print(f"A tool call failed: {str(error)}")
#     return f"❌ Sorry, tool failed: {str(error)}"

# @function_tool(failure_error_function=my_custom_error_function)
# async def plus(n1: int, n2: int) -> str:
#     if n1 < 0 or n2 < 0:
#         raise ValueError("Negative numbers not allowed.")
#     print("Tool Plus")
#     return f"✅ Your sum is {n1 + n2}"