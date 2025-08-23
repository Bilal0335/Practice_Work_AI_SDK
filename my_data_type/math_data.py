
# ! math_data.py
from pydantic import BaseModel

# ---- Math data ----
class SimpleResult(BaseModel):
    operation: str          # Tool name (plus/subtract/multiply/fetch_weather)
    input_values: list[int] # Inputs (numbers)
    result: str             # Tool output
    
class ToolMyScehma(BaseModel):
    n1:int
    n2:int