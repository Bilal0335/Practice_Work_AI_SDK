from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel

key = config("OPENRIUTER_API_KEY")
base_url = config("BASE_URL_OPENRIUTER")

openrouter_client = AsyncOpenAI(
    api_key=key,
    base_url=base_url
)

OPENROUTER_MODEL = OpenAIChatCompletionsModel(
    openai_client=openrouter_client,
    model="deepseek/deepseek-r1-0528-qwen3-8b:free"
)