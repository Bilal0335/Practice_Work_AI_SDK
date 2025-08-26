# ! clone_agent.py
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL
from agents import Agent, ModelSettings
from my_tool.math_tool import plus, subtract, calculate_area, get_weather

# * Base agent (❌ no tools here)
# base_agent = Agent(
#     name="Helper",
#     instructions="You are a general assistant.",
#     model_settings=ModelSettings(temperature=0.7),
#     model=GROQ_MODEL
# )

# * Clone with different instructions
# poet = base_agent.clone(
#     name="Poet",
#     instructions="You reply in poetry form.",
#     model_settings=ModelSettings(temperature=0.9)
# )

# scientist = base_agent.clone(
#     name="Scientist",
#     instructions="You reply with scientific facts.",
#     model_settings=ModelSettings(temperature=0.1)
# )

# * Weather agent (✅ tools explicitly added)
# weather_agent = base_agent.clone(
#     name="WeatherAssistant",
#     tools=[calculate_area, get_weather],
#     instructions="You are a weather and math assistant."
# )

# * Math agent (✅ tools explicitly added)
# math_agent = base_agent.clone(
#     name="MathAssistant",
#     tools=[calculate_area],
#     instructions="You are a math specialist."
# )



# * Base agent with basic tools
# base_agent = Agent(
#     name="BaseAssistant",
#     tools=[calculate_area],
#     instructions="You are a helpful assistant.",
#     model=GROQ_MODEL,
#     model_settings=ModelSettings(temperature=0.7)
# )

# * Multiple clones
# multiple_agents = {
#     "Weather": base_agent.clone(
#         name="WeatherAssistant",
#         tools=[calculate_area, get_weather],
#         instructions="You are a weather and math assistant."
#     ),
#     "Math": base_agent.clone(
#         name="MathAssistant",
#         tools=[calculate_area],
#         instructions="You are a math specialist.",
#         model_settings=ModelSettings(temperature=0.2)
#     ),
#     "Creative": base_agent.clone(
#         name="CreativeWriter",
#         instructions="You are a creative writer. Use vivid language.",
#         model_settings=ModelSettings(temperature=0.9)
#     ),
#     "Precise": base_agent.clone(
#         name="PreciseAssistant", 
#         instructions="You are a precise assistant. Be accurate and concise.",
#         model_settings=ModelSettings(temperature=0.1)
#     ),
# }


# * Demonstrate shared references
# ! clone_agents.py
from my_tool.math_tool import calculate_area


# --- Original agent ---
original_agent = Agent(
    name="OriginalAgent",
    tools=[calculate_area],
    instructions="You are a helpful assistant.",
    model=GROQ_MODEL
)

# --- Clone (general) ---
clone_agent = original_agent.clone(
    name="CloneAgent",
    instructions="You are a creative assistant."
)

# --- Shared clone (shares tools reference) ---
shared_clone = original_agent.clone(
    name="SharedClone",
    instructions="You share tools with Original."
)

# --- Independent clone (own tools list) ---
independent_clone = original_agent.clone(
    name="IndependentClone",
    tools=[calculate_area],  # only area tool
    instructions="You are an independent assistant."
)




