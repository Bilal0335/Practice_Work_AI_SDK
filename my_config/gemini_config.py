
# ! gemini_config
from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled

set_tracing_disabled(disabled=True)

key = config("GEMINI_API_KEY")
base_url = config("BASE_URL_GEMINI")

gemini_client = AsyncOpenAI(
    api_key=key,
    base_url=base_url
) # provider connection (Gemini API se link).

GEMINI_MODEL = OpenAIChatCompletionsModel(
    openai_client=gemini_client,
    model="gemini-2.5-flash",
    # model="gemini-2.5-flash-lite",
    # model="gemini-2.0-flash-lite",
    
) # model configuration (kis model ko chalana hai us provider pe).


# AsyncOpenAI → tum ek custom client bana rahe ho jo Gemini ke API endpoint aur API key use karega.

# OpenAIChatCompletionsModel → us client ko ek model wrapper ke sath attach kar rahe ho.

# GEMINI_MODEL → ye final object tum agent ko doge, aur agent directly Gemini se baat karega.