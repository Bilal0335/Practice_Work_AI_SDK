

# ! run_config.py

from agents import RunConfig
from my_config.gemini_config import gemini_client,GEMINI_MODEL

config_gemini = RunConfig(
    model=GEMINI_MODEL,
    model_provider=gemini_client
)

# * Run Level → ek specific run() ke waqt manually model/provider set karte ho.