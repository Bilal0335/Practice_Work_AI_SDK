

# ! weather_data.py

# ---- Weather Data ----
from pydantic import BaseModel

class Location(BaseModel):
    lat: float
    long: float
    

class WeatherResult(BaseModel):
    city: str
    temperature: str
    condition: str