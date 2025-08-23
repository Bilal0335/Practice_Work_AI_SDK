
# ! run_result.py
from agents import Runner
# from my_agent.teacher_agent import groq_agent


# teacher_res = Runner.run_sync(
#     starting_agent=teacher,
#     input="2+2=?"
# )

# print(teacher_res.final_output)

# ! Global Level
from agents import set_default_openai_api,set_default_openai_client
from my_config.gemini_config import gemini_client
from my_config.groq_config import groq_client
from my_agent.teacher_agent import groq_agent


set_default_openai_api("chat_completions")
set_default_openai_client(gemini_client)

teacher_res = Runner.run_sync(
    starting_agent=groq_agent,
    input="2+2=?"
)

print(teacher_res.final_output)


# ! run level
# from my_run_config.run_config import config_gemini
# teacher_res = Runner.run_sync(
#     starting_agent=groq_agent,
#     input="2+2=?",
#     run_config=config_gemini
# )
# # → Gemini model chalega

# print("GEMINI CONFIG: ",teacher_res.final_output)


# ! Run Level → ek hi agent ko run karte waqt provider temporarily change karna.
