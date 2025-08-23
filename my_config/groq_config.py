from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled

set_tracing_disabled(disabled=True)

key = config("GROQ_API_KEY")
base_url = config("BASE_URL_GROQ")

groq_client = AsyncOpenAI(
    api_key=key,
    base_url=base_url
)

GROQ_MODEL = OpenAIChatCompletionsModel(
    openai_client=groq_client,
    model="llama-3.3-70b-versatile"
)