
# ! guardrails_agent.py

from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_data_type.output_data_guardrails import MyOutputGuardrail

guardrail_agent = Agent(
    name="Guardrail Checker",
    instructions="check  Hotel Sannata's queries and account or tax query.",
    model=GEMINI_MODEL,
    output_type=MyOutputGuardrail
)

# ---

# # 🔒 Guardrails kya hote hain?

# Guardrails ka kaam hai **extra check lagana** before (input) ya after (output) agent run karta hai.
# Soch lo jaise ek **security filter** jo parallel me chalta hai agent ke sath.

# * **Input Guardrail** → Agent ke run hone se pehle user ke input ko check karta hai.
# * **Output Guardrail** → Agent ke run hone ke baad uske jawab (output) ko check karta hai.

# Agar guardrail ko lagta hai ke input/output **rules tod raha hai**, to wo **tripwire trigger** kar deta hai → aur agent ka run **stop** kar diya jata hai.

# ---

# # 🛑 Tripwire kya hota hai?

# * Tripwire ek flag (switch) hai jo guardrail **true/false** karta hai.
# * Agar **tripwire\_triggered = True** ho gaya → iska matlab hai ke rule tod diya gaya hai, aur ek **exception** raise hogi (execution ruk jayega).

# So basically tripwire = "🚨 Alert: Rule violated".

# ---

# # 🔹 Input Guardrail (Before Agent Runs)

# **Use case**: Suppose ek expensive support agent hai. Aap chahte ho ke wo **math homework** solve na kare.
# So aap input pe guardrail lagate ho jo check kare: "Kya user ne math homework poocha hai?"

# ### Flow:

# 1. User input agent ko milta hai.
# 2. Guardrail function run hota hai aur ek result deta hai.
# 3. Agar result me `.tripwire_triggered = True` hai → **InputGuardrailTripwireTriggered** exception aati hai aur agent stop ho jata hai.

# ---

# ### Example (Math Homework Detector)

# ```python
# class MathHomeworkOutput(BaseModel):
#     is_math_homework: bool
#     reasoning: str
# ```

# * Ye ek schema hai jo guardrail agent ka output define karega.
# * `is_math_homework` batayega true/false.
# * `reasoning` explain karega kyun math homework laga.

# ```python
# guardrail_agent = Agent( 
#     name="Guardrail check",
#     instructions="Check if the user is asking you to do their math homework.",
#     output_type=MathHomeworkOutput,
# )
# ```

# * Ye ek chhota guardrail agent hai jo sirf check karega input math homework hai ya nahi.

# ```python
# @input_guardrail
# async def math_guardrail(ctx, agent, input):
#     result = await Runner.run(guardrail_agent, input, context=ctx.context)
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=result.final_output.is_math_homework,
#     )
# ```

# * Ye guardrail function hai.
# * Ye guardrail agent ko run karta hai aur uska output leta hai.
# * Agar `is_math_homework=True` ho gaya → tripwire trigger ho jata hai.

# ```python
# agent = Agent(  
#     name="Customer support agent",
#     instructions="You are a customer support agent. You help customers with their questions.",
#     input_guardrails=[math_guardrail],
# )
# ```

# * Ab asli agent ke sath input guardrail attach kar diya.

# ```python
# async def main():
#     try:
#         await Runner.run(agent, "Hello, can you help me solve for x: 2x + 3 = 11?")
#     except InputGuardrailTripwireTriggered:
#         print("Math homework guardrail tripped")
# ```

# * Jab user input me math homework detect hota hai → exception aati hai aur print hota hai "Math homework guardrail tripped".

# ---

# # 🔹 Output Guardrail (After Agent Runs)

# **Use case**: Aap chahte ho ke agent **math ka jawab** na de, chahe input kuch bhi ho.
# So agent ka jawab (output) bhi guardrail ke through check hota hai.

# ### Flow:

# 1. Agent normal jawab generate karega.
# 2. Guardrail us jawab ko check karega.
# 3. Agar jawab me math hua → `.tripwire_triggered=True` aur agent ka jawab stop.

# ---

# ### Example (Math Output Detector)

# ```python
# class MessageOutput(BaseModel): 
#     response: str
# ```

# * Asli agent ka output type (sirf ek response).

# ```python
# class MathOutput(BaseModel): 
#     reasoning: str
#     is_math: bool
# ```

# * Guardrail agent ka output type (ye check karega jawab math hai ya nahi).

# ```python
# guardrail_agent = Agent(
#     name="Guardrail check",
#     instructions="Check if the output includes any math.",
#     output_type=MathOutput,
# )
# ```

# * Ek guardrail agent jo check karega jawab me math hai ya nahi.

# ```python
# @output_guardrail
# async def math_guardrail(ctx, agent, output: MessageOutput):
#     result = await Runner.run(guardrail_agent, output.response, context=ctx.context)
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=result.final_output.is_math,
#     )
# ```

# * Guardrail function agent ke jawab ko analyze karega.
# * Agar jawab me `is_math=True` → tripwire trigger ho jayega.

# ```python
# agent = Agent( 
#     name="Customer support agent",
#     instructions="You are a customer support agent. You help customers with their questions.",
#     output_guardrails=[math_guardrail],
#     output_type=MessageOutput,
# )
# ```

# * Asli agent ke sath output guardrail attach kar diya.

# ```python
# async def main():
#     try:
#         await Runner.run(agent, "Hello, can you help me solve for x: 2x + 3 = 11?")
#     except OutputGuardrailTripwireTriggered:
#         print("Math output guardrail tripped")
# ```

# * Ab chahe user input normal ho, agar agent jawab me math deta hai → guardrail trip ho jata hai.

# ---

# # 🔑 Key Points to Remember

# 1. **Input Guardrail** = Input check karta hai (pehle).
# 2. **Output Guardrail** = Output check karta hai (baad me).
# 3. **Tripwire** = True hone pe exception throw hoti hai → agent stop.
# 4. **Guardrail Function** = Special function hota hai jo `GuardrailFunctionOutput` return karta hai.
# 5. **Guardrail Agent** = Chhota helper agent hota hai jo check karega (math detect, toxic language detect, etc).

# ---

# ✅ Is tarah se guardrails ek **extra safety layer** banate hain, jo agents ko galat ya unwanted kaam karne se rokta hai.

# ---