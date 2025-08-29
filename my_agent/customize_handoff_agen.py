# # ! customize_handoff_agent.py

# import rich
# from my_config.groq_config import GROQ_MODEL
# from agents import Agent, ModelSettings, handoff, enable_verbose_stdout_logging
# from my_tool.math_tool import plus,get_weather
# from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
# from my_service.service_cus_handoff import service
# from my_data_type.custom_handoff_data import MathReasoning
# # Enable verbose logging for debugging
# # enable_verbose_stdout_logging()

# # * Math Agent
# math_agent = Agent(
#     name="Math_Agent",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX} 
# You are a math assistant. Help with calculations, problem-solving, and explanations.""",
#     model_settings=ModelSettings(temperature=0.7),
#     model=GROQ_MODEL,
#     tools=[plus],
#     handoff_description="Handles all math-related tasks and calculations."
# )

# # * Math handoff customization
# math_teacher = handoff(
#     agent=math_agent,
#     tool_name_override="math_teacher",
#     tool_description_override="This is a math teacher specialized in solving math problems.",
#     # on_handoff=service,
#     # on_handoff=lambda ctx, data: rich.print(data.reasoning),
#     on_handoff=lambda ctx, data: print(f"Question: {data.question}\nReason: {data.reasoning}\n"),
#     input_type=MathReasoning
# )

# # * English Agent
# english_agent = Agent(
#     name="English_Agent",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX} 
# You are an English assistant. Help with grammar, vocabulary, and explanations.""",
#     model_settings=ModelSettings(temperature=0.2),
#     model=GROQ_MODEL,
#     handoff_description="Handles English-related tasks like grammar and writing help."
# )

# # * English handoff customization
# english_teacher = handoff(
#     agent=english_agent,
#     tool_name_override="english_teacher",
#     tool_description_override="This is an English teacher specialized in grammar and language help."
# )

# # * Main / triage agent with handoffs
# assistant_agent = Agent(
#     name="Assistant_Agent",
#     instructions="You are a general assistant. If the user query is math-related, hand it off to math_teacher. If it's English-related, hand it off to english_teacher.",
#     model_settings=ModelSettings(temperature=0.7),
#     model=GROQ_MODEL,
#     handoffs=[math_teacher, english_teacher],
#     tools=[get_weather]
# )

# # Debug print: show registered handoffs
# rich.print("[bold underline green]Registered Handoffs:[/bold underline green]")
# for h in assistant_agent.handoffs:
#     rich.print(f"[bold cyan]Tool Name:[/bold cyan] {h.tool_name}")
#     rich.print(f"[bold yellow]Tool Description:[/bold yellow] {h.tool_description}")
#     rich.print(f"[bold magenta]Agent Name:[/bold magenta] {h.agent_name}")
#     rich.print("-" * 60)


# # for h in assitant_agent.handoffs:
# #     rich.print(f"[bold cyan]Tool Name:[/bold cyan] {h.tool_name}")
# #     rich.print(f"[bold yellow]Tool Description:[/bold yellow] {h.tool_description}")
# #     rich.print(f"[bold magenta]Agent Name:[/bold magenta] {h.agent_name}")
# #     rich.print("-" * 60)



# * customize_handoff_agent.py
# import rich
# from agents import Agent, ModelSettings, handoff, enable_verbose_stdout_logging
# from my_tool.math_tool import plus, get_weather
# from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
# from my_data_type.custom_handoff_data import MathReasoning
# from my_config.groq_config import GROQ_MODEL
# from my_service.service_cus_handoff import service
# Uncomment for verbose logs
# enable_verbose_stdout_logging()

# * --- Math Agent ---
# math_agent = Agent(
#     name="Math_Agent",
#     instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are a math assistant. Help with calculations, problem-solving, and explanations.",
#     model_settings=ModelSettings(temperature=0.7),
#     model=GROQ_MODEL,
#     tools=[plus],
#     handoff_description="Handles all math-related tasks and calculations."
# )

# * Math Handoff
# math_teacher = handoff(
#     agent=math_agent,
#     tool_name_override="math_teacher",
#     tool_description_override="This is a math teacher specialized in solving math problems.",
#     input_type=MathReasoning,
#     on_handoff=service
#     # on_handoff=lambda ctx, data: rich.print(f"[cyan]Question:[/cyan] {data.question}\n[green]Reason:[/green] {data.reasoning}\n")
# )

# * --- English Agent ---
# english_agent = Agent(
#     name="English_Agent",
#     instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are an English assistant. Help with grammar, vocabulary, and explanations.",
#     model_settings=ModelSettings(temperature=0.2),
#     model=GROQ_MODEL,
#     handoff_description="Handles English-related tasks like grammar and writing help."
# )

# english_teacher = handoff(
#     agent=english_agent,
#     tool_name_override="english_teacher",
#     tool_description_override="This is an English teacher specialized in grammar and language help."
# )

# # * --- Main Assistant Agent ---
# assistant_agent = Agent(
#     name="Assistant_Agent",
#     instructions="You are a general assistant. If the user query is math-related, hand it off to math_teacher. If it's English-related, hand it off to english_teacher.",
#     model_settings=ModelSettings(temperature=0.7),
#     model=GROQ_MODEL,
#     handoffs=[math_teacher, english_teacher],
#     tools=[get_weather]
# )

# Debug: print all registered handoffs
# rich.print("[bold underline green]Registered Handoffs:[/bold underline green]")
# for h in assistant_agent.handoffs:
#     rich.print(f"[bold cyan]Tool Name:[/bold cyan] {h.tool_name}")
#     rich.print(f"[bold yellow]Tool Description:[/bold yellow] {h.tool_description}")
#     rich.print(f"[bold magenta]Agent Name:[/bold magenta] {h.agent_name}")
#     rich.print("-" * 50)



# ! customize_handoff_agent.py
# final working

from agents import Agent,ModelSettings,handoff
import rich
from my_config.gemini_config import GEMINI_MODEL
from my_tool.math_tool import get_weather, plus
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from my_service.service_cus_handoff import service
from my_data_type.custom_handoff_data import MathReasoning
from agents.extensions import handoff_filters
from my_custom_handoff_policy.policy import en

# * --- Math Agent ---
math_agent = Agent(
    name="Math_Agent",
    instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are a math assistant. Help with calculations, problem-solving, and explanations.",
    model_settings=ModelSettings(temperature=0.7),
    model=GEMINI_MODEL,
    tools=[plus],
    handoff_description="Handles all math-related tasks and calculations."
)

# * Math Handoff
math_teacher = handoff(
    agent=math_agent,
    tool_name_override="math_teacher",
    tool_description_override="This is a math teacher specialized in solving math problems.",
    input_type=MathReasoning,
    on_handoff=service,
    input_filter=handoff_filters.remove_all_tools,
    is_enabled=en
    
    # is_enabled=False  #deactive
    # on_handoff=lambda ctx, data: rich.print(f"[cyan]Question:[/cyan] {data.question}\n[green]Reason:[/green] {data.reasoning}\n")
)

# * --- English Agent ---
english_agent = Agent(
    name="English_Agent",
    instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are an English assistant. Help with grammar, vocabulary, and explanations.",
    model_settings=ModelSettings(temperature=0.2),
    model=GEMINI_MODEL,
    handoff_description="Handles English-related tasks like grammar and writing help."
)

# english_teacher = handoff(
#     agent=english_agent,
#     tool_name_override="english_teacher",
#     tool_description_override="This is an English teacher specialized in grammar and language help."
# )

# * --- Main Assistant Agent ---
assistant_agent = Agent(
    name="Assistant_Agent",
    instructions="""
        You are a general assistant.
        - If the user asks a math-related question, hand it off to math_teacher.
        - If the user asks an English-related question, hand it off to english_teacher.
        - If the user asks about the weather in a city, ALWAYS use the get_weather tool
        and include its output in your final answer.
        Combine answers if user asks for both math and weather in one query.
    """,
    model_settings=ModelSettings(temperature=0.7),
    model=GEMINI_MODEL,
    handoffs=[math_teacher],   # sirf math ka handoff
    tools=[get_weather]  ,
)

rich.print(assistant_agent.handoffs)














# 🔑 Pehle Basic Idea:

# Handoff ka matlab hai:
# Agar ek agent (assistant) ke paas query aayi hai aur wo sochta hai ke ye kaam uske liye nahi hai, to wo "handoff" karke dusre specialized agent ko transfer kar deta hai.

# Example:

# Triage Agent (general) → Billing Agent (specialist)

# Assistant Agent → Math Agent

# ⚙️ handoff() function me kya hota hai?

# Ye ek function hai jo ek "handoff tool" banata hai jo ek agent ke andar attach ho jata hai.

# Parameters ka role:

# agent

# Ye woh specialist agent hai jisko aap handoff karna chahte ho.

# Example: billing_agent, math_agent

# tool_name_override

# By default tool ka naam hota hai: transfer_to_<agent_name>.

# Agar aap chahe to apna naam de sakte ho.

# Example: "escalate_to_specialist"

# tool_description_override

# Default me ek simple description hoti hai.

# Aap isko override karke LLM ko clearer instructions de sakte ho.

# Example: "Use this for complex issues that require a specialist."

# on_handoff

# Ye ek callback function hai jo turant trigger hota hai jab handoff initiate hota hai.

# Matlab → "jaise hi transfer hua, ek extra kaam kar lo" (jaise logging, database entry, alert, etc.)

# Is function ko ctx (context) milta hai, aur agar aap input_type use karte ho to LLM se structured data bhi milta hai.

# input_type

# Ye sabse powerful cheez hai.

# Ye define karta hai ke jab LLM handoff kare, usko structured data (Pydantic model) bhi dena hoga.

# Example:

# class EscalationData(BaseModel):
#     reason: str
#     order_id: str


# Matlab → Jab handoff hoga, LLM ko ye dono fields fill karke deni hongi.

# input_filter

# By default, naya agent puri conversation history dekh sakta hai.

# Lekin agar aap chahte ho ke usko sirf user ka question mile (aur tools ka clutter na jaye), to input_filter use karte ho.

# Example: handoff_filters.remove_all_tools

# is_enabled

# Handoff ko dynamically enable/disable kar sakte ho.

# Example: Agar system down hai, to "transfer_to_refund_agent" temporarily disable kar do.