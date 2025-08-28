

# ! math_tool.py

from agents import function_tool
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

@function_tool(name_override="get_weather_args")  # 👈 force tool name
def get_weather(city: str) -> str:
    """Get weather info for a city."""
    print("[yellow]=== Tool Used: Weather ===[/yellow]")
    return f"Weather in {city}: Sunny, 72°F"

# @function_tool
# def get_weather(city: str) -> str:
#     return f"Weather in {city}: Sunny, 72°F"

# --- Extra demo tool ---
@function_tool
def new_tool() -> str:
    """A new demo tool"""
    return "I'm a new tool!"