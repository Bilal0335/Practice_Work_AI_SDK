

# ! math_tool.py

from agents import function_tool,FunctionToolResult,ToolsToFinalOutputResult
from rich import print


@function_tool
async def plus(n1: int, n2: int) -> str:
    """This is a Plus Function.
    
    Args:
        n1 (int): First number
        n2 (int): Second number
        
    Returns:
        str: The sum in string format
    """
    print("[green]=== Tool Used: PLUS ===[/green]")
    return f"your sum is {n1 + n2}"


@function_tool
async def subtract(n1: int, n2: int) -> str:
    """This is a Subtract Function.
    
    Args:
        n1 (int): First number
        n2 (int): Second number
        
    Returns:
        str: The subtraction result in string format
    """
    print("[yellow]=== Tool Used: SUBTRACT ===[/yellow]")
    return f"your result is {n1 - n2}"

@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate the area of a rectangle."""
    area = length * width
    return f"Area = {length} × {width} = {area} square units"

@function_tool
async def multiply(n1: int, n2: int) -> str:
    """This is a Multiply Function.
    
    Args:
        n1 (int): First number
        n2 (int): Second number
        
    Returns:
        str: The multiplication result in string format
    """
    print("[blue]=== Tool Used: MULTIPLY ===[/blue]")
    return f"your result is {n1 * n2}"


@function_tool
def calculate_area(length: float, width: float) -> str:
    return f"Area = {length * width} square units"

# @function_tool
# def get_weather(city: str) -> str:
#     """
#     Get the weather info for a given city.

#     Args:
#         city (str): The name of the city (e.g., "Karachi", "London").
    
#     Returns:
#         str: Weather description for that city.
#     """
#     print("[yellow]=== Tool Used: Weather ===[/yellow]")
#     return f"Weather in {city}: Sunny, 72°F"


@function_tool
def get_weather(city: str) -> str:
    print("[yellow]=== Tool Used: Weather ===[/yellow]")
    return f"Weather in {city}: Sunny, 72°F"

# --- Extra demo tool ---
@function_tool
def new_tool() -> str:
    """A new demo tool"""
    return "I'm a new tool!"

def my_behavior(context, tool_results: list[FunctionToolResult]):
    rich.print("\n[bold green]=== Custom Tool Use Behavior Called ===[/bold green]")
    # rich.print("Context:", context)
    # rich.print("Tool Results:", tool_results)

    tool_name = tool_results[0].tool.name
    tool_output = tool_results[0].output

    if tool_name == "get_time":
        return ToolsToFinalOutputResult(
            is_final_output=True,
            final_output=f"[CUSTOM] Time tool returned: {tool_output}",
        )
    elif tool_name == "plus":
        return ToolsToFinalOutputResult(
            is_final_output=True,
            final_output=f"[CUSTOM] Plus tool ne ye result diya: {tool_output}",
        )
    else:
        return ToolsToFinalOutputResult(
            is_final_output=False,
            final_output=None,
        )
