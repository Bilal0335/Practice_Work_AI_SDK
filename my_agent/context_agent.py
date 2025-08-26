# from my_config.groq_config import GROQ_MODEL
# from agents import Agent
# from my_tool.context_tool import fetch_user_age
# from instruction.dynamic_instruction import dynamic_instructions
# from my_data_type.context_data import userData


# context_agents: Agent = Agent[userData](
#     name="context_agents",
#     # instructions=(
#     #     "You are a helpful assistant. "
#     #     "If the user asks about their age, always use the fetch_user_age tool. "
#     #     "Do not answer age questions without calling the tool."
#     # ),
#     instructions=dynamic_instructions,
#     model=GROQ_MODEL,
#     tools=[fetch_user_age]
# )

from agents import Agent
from my_data_type.context_data import UserData
from my_tool.context_tool import fetch_user_age, recommend_study_plan, motivate_user
from my_config.groq_config import GROQ_MODEL
from instruction.dynamic_instruction import dynamic_instructions

# Define the main agent with context + tools
context_agents: Agent[UserData] = Agent[UserData](
    name="study_assistant",
    instructions=dynamic_instructions,
    model=GROQ_MODEL,
    tools=[fetch_user_age, recommend_study_plan, motivate_user]
)



# # 📘 Context Management in OpenAI Agents SDK

# ## 🔹 Definition

# Context management = extra data ko handle karna jo aapka code (tools, lifecycle hooks, callbacks) use kar sakta hai **during agent execution**.

# 👉 Do main types hote hain:

# 1. **Local Context**
# 2. **Agent/LLM Context**

# ---

# ## 1️⃣ Local Context

# ### What It Is:

# * Internal data jo **sirf backend ke liye hoti hai** (LLM ko nahi bheji jaati).
# * Ek Python object (dataclass / Pydantic model) me store hoti hai.
# * Har run ke tools, hooks, callbacks isse access kar sakte hain.

# ### How It Works:

# * **Create**: ek dataclass/Pydantic model banao (e.g. `UserInfo(name, uid)`).
# * **Pass**: `Runner.run(..., context=your_context)` ke zariye bhejo.
# * **Access**: tool function me `wrapper.context` se access karte ho.

# ### Key Point:

# * **Consistency**: ek run ke andar hamesha ek hi type ka context hona chahiye.

# ### Example Use Cases:

# * User details store karna (ID, username).
# * Logger ya helper functions inject karna.
# * Temporary run data rakhna.

# ### 🚫 Not Sent to LLM

# * Yeh data **LLM ko dikhaya nahi jaata**. Sirf tools aur backend logic use karte hain.

# ---

# ## 2️⃣ Agent/LLM Context

# ### What It Is:

# * Wo information jo **LLM ko input me dikhai jaati hai**.
# * Basically conversation history + system prompt + instructions + user input.

# ### How To Use:

# * **Embedding in Instructions**: agent ke instructions me data add karna (e.g. “User’s name is Ali”).
# * **Passing in Input**: input me extra info dena (e.g. `"Today is Monday, plan accordingly"`).
# * **Function Tools**: LLM tool call karke runtime data le sakta hai.
# * **Retrieval/Web Search**: bahar se data fetch karke LLM ko provide karna.

# ### Key Difference:

# * Local Context → hidden (backend only)
# * Agent/LLM Context → visible to LLM

# ---

# ## 🔹 Code Example (Simplified)

# ```python
# from dataclasses import dataclass
# from agents import Agent, RunContextWrapper, Runner, function_tool

# @dataclass
# class UserInfo:
#     name: str
#     uid: int

# @function_tool
# async def fetch_user_age(ctx: RunContextWrapper[UserInfo]):
#     return f"User {ctx.context.name} is 47 years old"

# user_info = UserInfo(name="John", uid=123)

# agent = Agent[UserInfo](
#     name="Assistant",
#     tools=[fetch_user_age],
# )

# result = Runner.run_sync(
#     starting_agent=agent,
#     input="What is the age of the user?",
#     context=user_info
# )

# print(result.final_output)
# ```

# ---

# ## 🔹 Explanation of Example

# 1. **Local Context**

#    * `UserInfo(name="John", uid=123)` bana.
#    * `context=user_info` pass hua run ke andar.
#    * Tool ne `ctx.context.name` use karke John ka data access kiya.
#    * Yeh info LLM ko nahi bheja gaya.

# 2. **Agent/LLM Context**

#    * Input `"What is the age of the user?"` LLM ko gaya.
#    * Agar hum instructions me `"The user’s name is John"` likhte, toh yeh LLM ko dikh jata.

# ---

# ## ✍️ Exam-Ready Notes (Short Form)

# * **Context Management** = handling extra data in agents run.
# * **Types**:

#   * Local Context → backend only, not visible to LLM.
#   * Agent/LLM Context → part of prompt, visible to LLM.
# * **Local Context Examples**: userID, logger, helper functions.
# * **LLM Context Examples**: system prompt, chat history, extra instructions.
# * **Key Difference**: Local = hidden, LLM Context = exposed.
# * **Code Flow**: dataclass → context pass → tool access via `ctx.context`.

# ---

