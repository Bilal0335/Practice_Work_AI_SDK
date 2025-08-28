
# ! handoff_agent.py

# from my_config.groq_config import GROQ_MODEL
# from agents import Agent, ModelSettings
# from my_tool.math_tool import plus

# # Math agent
# math_agent = Agent(
#     name="Math_Agent",
#     instructions="You are a math assistant.",
#     model_settings=ModelSettings(temperature=0.7),
#     model=GROQ_MODEL,
#     tools=[plus]
# )

# # English agent
# english_agent = Agent(
#     name="English_Agent",
#     instructions="You are an english assistant.",
#     model_settings=ModelSettings(temperature=0.2),
#     model=GROQ_MODEL,
#     tools=[plus]
# )

# # Main / triage agent with handoffs
# assitant_agent = Agent(
#     name="Assistant_Agent",
#     instructions="You are a general assistant. Delegate math or english tasks.",
#     model_settings=ModelSettings(temperature=0.7),
#     model=GROQ_MODEL,
#     handoffs=[math_agent, english_agent]  # ✅ ab yahan use kar sakte ho
# )

# ! pratice work
# from my_config.groq_config import GROQ_MODEL
# from agents import Agent, ModelSettings
# from my_tool.math_tool import plus
# from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
# import rich

# * Base agent (no handoffs yet)
# base_agent = Agent(
#     name="Base_Agent",
#     instructions="You are a base agent.",
#     model_settings=ModelSettings(temperature=0.7),
#     model=GROQ_MODEL,
# )

# * Specialist agents (clones of base_agent)
# math_agent = base_agent.clone(
#     name="Math_Agent",
#     # instructions="You are a math assistant.",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
#     You are a math assistant.""",
#     tools=[plus],
#     handoff_description="This is a math teacher."
# )

# english_agent = base_agent.clone(
#     name="English_Agent",
#     # instructions="You are an english assistant.",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX} 
#     You are a english assistant.""",
#     handoff_description="This is a math teacher."
# )

# * Main agent with handoffs
# assistant_agent = base_agent.clone(
#     name="Assistant_Agent",
#     instructions="You are a general assistant. Delegate to math or english agents.",
#     handoffs=[math_agent, english_agent]
# )


# rich.print(assistant_agent.handoffs)


# for h in assistant_agent.handoffs:
#     rich.print(f"[bold green]Handoff Agent:[/bold green] {h.name}")
#     rich.print(f"[yellow]Description:[/yellow] {h.handoff_description}")
#     print("-" * 40)




# !practice_work.py
from my_config.groq_config import GROQ_MODEL
from agents import Agent, handoff

# * --- Specialist Agents ---
# billing_agent = Agent(
#     name="Billing agent",
#     instructions="Handle billing questions.",
#     model=GROQ_MODEL
# )

# refund_agent = Agent(
#     name="Refund agent",
#     instructions="Handle refunds.",
#     model=GROQ_MODEL
# )

# * --- Triage Agent with Handoffs ---
# triage_agent = Agent(
#     name="Triage agent",
#     instructions=(
#         "Help the user with their questions. "
#         "If they ask about billing, handoff to the Billing agent. "
#         "If they ask about refunds, handoff to the Refund agent."
#     ),
#     handoffs=[billing_agent, handoff(refund_agent)],
#     model=GROQ_MODEL
# )
# ! PRATICE WORK
# *Fitness Coach 
fitness_coach = Agent(
    name="Fitness Coach",
    instructions=(
        "You're a running coach. Ask 1-2 quick questions, then give a week plan. "
        "Keep it simple and encouraging. No medical advice."
    ),
    model=GROQ_MODEL
)

# * Study Coach
study_coach = Agent(
    name="Study Coach",
    instructions=(
        "You're a study planner. Ask for current routine, then give a 1-week schedule. "
        "Keep steps small and doable."
    ),
    model=GROQ_MODEL
)

# * Router that decides who should OWN the conversation
router = Agent(
    name="Coach Router",
    instructions=(
        "Route the user:\n"
        "- If message is about running, workout, stamina → handoff to Fitness Coach.\n"
        "- If it's about exams, study plan, focus, notes → handoff to Study Coach.\n"
        "After handoff, the specialist should continue the conversation."
    ),
    handoffs=[study_coach, handoff(fitness_coach)],
    model=GROQ_MODEL
)


# ! learn
# * 1. Handoff kya hota hai?

# Handoff ka matlab hai ek agent se dusre agent ko query forward karna.
# Example:

# Assistant_Agent → user query dekhta hai → decide karta hai ye math ka kaam hai → phir Math_Agent ko forward kar deta hai.

# Isi process ko handoff kehte hain.

# * 🔹 2. RECOMMENDED_PROMPT_PREFIX kya karta hai?

# Ye ek extra prefix text hai jo tumhare agent ke instructions me automatically add ho jata hai.
# Iska purpose hai LLM ko sikhana / remind karna ke handoff system exist karta hai aur kaise behave karna hai.

# Matlab agar tum seedha likho:

# * instructions="You are a math assistant."


# toh model ko bas math related kaam samajh aayega.

# Lekin agar tum likho:

# * instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
# You are a math assistant."""


# toh model ke paas ye extra context hota hai:

# Handoffs kaise kaam karte hain

# Kab dusre agents ko refer karna hai

# Apni responsibility clear karna

# * 🔹 4. Without vs With RECOMMENDED_PROMPT_PREFIX

# Without prefix:

# You are a math assistant.


# ⚠️ Model kabhi kabhi delegate karna bhool sakta hai ya irrelevant answer de sakta hai.

# With prefix:

# Recommended system message about handoffs
# You are a math assistant.


# ✅ Model zyada accurately handoff follow karega.