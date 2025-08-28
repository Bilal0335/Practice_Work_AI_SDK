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



# customize_handoff_agent.py
import rich
from agents import Agent, ModelSettings, handoff, enable_verbose_stdout_logging
from my_tool.math_tool import plus, get_weather
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from my_data_type.custom_handoff_data import MathReasoning
from my_config.groq_config import GROQ_MODEL
from my_service.service_cus_handoff import service
# Uncomment for verbose logs
# enable_verbose_stdout_logging()

# --- Math Agent ---
math_agent = Agent(
    name="Math_Agent",
    instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are a math assistant. Help with calculations, problem-solving, and explanations.",
    model_settings=ModelSettings(temperature=0.7),
    model=GROQ_MODEL,
    tools=[plus],
    handoff_description="Handles all math-related tasks and calculations."
)

# Math Handoff
math_teacher = handoff(
    agent=math_agent,
    tool_name_override="math_teacher",
    tool_description_override="This is a math teacher specialized in solving math problems.",
    input_type=MathReasoning,
    on_handoff=service
    # on_handoff=lambda ctx, data: rich.print(f"[cyan]Question:[/cyan] {data.question}\n[green]Reason:[/green] {data.reasoning}\n")
)

# --- English Agent ---
english_agent = Agent(
    name="English_Agent",
    instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are an English assistant. Help with grammar, vocabulary, and explanations.",
    model_settings=ModelSettings(temperature=0.2),
    model=GROQ_MODEL,
    handoff_description="Handles English-related tasks like grammar and writing help."
)

english_teacher = handoff(
    agent=english_agent,
    tool_name_override="english_teacher",
    tool_description_override="This is an English teacher specialized in grammar and language help."
)

# --- Main Assistant Agent ---
assistant_agent = Agent(
    name="Assistant_Agent",
    instructions="You are a general assistant. If the user query is math-related, hand it off to math_teacher. If it's English-related, hand it off to english_teacher.",
    model_settings=ModelSettings(temperature=0.7),
    model=GROQ_MODEL,
    handoffs=[math_teacher, english_teacher],
    tools=[get_weather]
)

# Debug: print all registered handoffs
# rich.print("[bold underline green]Registered Handoffs:[/bold underline green]")
# for h in assistant_agent.handoffs:
#     rich.print(f"[bold cyan]Tool Name:[/bold cyan] {h.tool_name}")
#     rich.print(f"[bold yellow]Tool Description:[/bold yellow] {h.tool_description}")
#     rich.print(f"[bold magenta]Agent Name:[/bold magenta] {h.agent_name}")
#     rich.print("-" * 50)
