

# ! tool_control_agent.py

from agents import Agent,ModelSettings
from agents.agent import StopAtTools
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL
from my_tool.math_tool import plus,subtract,multiply,my_behavior


tool_control_agents = Agent(
    name="tool_control_agents",
    instructions="You are helpfull tool_control_agents",
    tools=[plus,subtract,multiply],
    model=GEMINI_MODEL,
    # tool_use_behavior="run_llm_again",
    # tool_use_behavior="stop_on_first_tool",
    # tool_use_behavior=StopAtTools(stop_at_tool_names=['subtract']),
    # tool_use_behavior=StopAtTools(stop_at_tool_names=['plus','multiply']),
    tool_use_behavior=my_behavior,
    
    # model_settings=ModelSettings(tool_choice="auto"),
    # model_settings=ModelSettings(tool_choice="none"),
    # model_settings=ModelSettings(tool_choice="required"),
    # model_settings=ModelSettings(tool_choice="multiply"),
    # model_settings=ModelSettings(tool_choice="subtract",temperature=0),
    model_settings=ModelSettings(tool_choice="subtract",parallel_tool_calls=False),
    reset_tool_choice=True
)

math_tutor = Agent(
    name="Math Tutor",
    instructions="You are a precise math tutor. Always show your work step by step.",
    model_settings=ModelSettings(
        temperature=0.1,  # Very focused
        max_tokens=500    # Enough for detailed steps
    ),
    model=GROQ_MODEL
)


creative_writer = Agent(
    name="Creative Writer",
    instructions="You are a creative storyteller. Write engaging, imaginative stories.",
    model_settings=ModelSettings(
        temperature=0.8,  # Very creative
        max_tokens=300    # Short but creative
    ),
    model=GROQ_MODEL
)

# More focused vocabulary Agent
focused_agent = Agent(
    name="Focused",
    instructions="You are a focused assistant. Use concise and diverse vocabulary.",
    model_settings=ModelSettings(
        top_p=0.3,              # Sirf top 30% vocab words ka use karega
        frequency_penalty=0.5,  # Repeat kam hoga
        presence_penalty=0.3    # Naye topics explore karega
    ),
    model=GROQ_MODEL
)


# ! tool_use_behavior

#! 1. "run_llm_again"
# * Tool result milne ke baad LLM dobara run hota hai aur polished jawab deta hai.

#! 2. "stop_on_first_tool"
# * Pehle tool ka result hi final output ban jata hai, LLM dobara nahi chalta.

#! 3. StopAtTools
# * 👉 “Agar listed tool call ho jaye to wahi ruk jao, aur us tool ka result hi final output banado. LLM dobara mat chalao.”
# * StopAtTools trigger hone ke baad agent dobara LLM nahi chalayega

# ! model_settings

#! 1. tool_choice="required"

#* LLM har hal me tool use karega, chahe input simple ho ya complex.

#* Output tool ke bina incomplete nahi hoga.

#* Example: Aapka "hello" input bhi agar tool relevant ho to call hoga.

#! 2. tool_choice="none"

#* LLM tool completely ignore karega, sirf apni reasoning se answer generate karega.

#* Tools ka result output me kabhi nahi aayega.

#! 3. tool_choice="auto"

#* LLM khud decide karega ke kaunsa tool use karna hai.

#* Mostly instruction sequence follow karta hai, lekin exact order guarantee nahi.

#* Random nahi hota, intelligent decision based on input aur context hota hai.

#! 7.**`model_settings = ModelSettings(tool_choice="subtract")`**

# * LLM ko **subtract tool use karna prefer karne** ke liye kaha ja raha hai.
# * Mostly **har run me subtract tool chalega**, lekin:

#   * Agar `StopAtTools` me subtract nahi hai → LLM **dobara run ho sakta hai** aur dusre tools bhi use kar sakta hai.
#   * Agar `temperature>0` → output me **thodi randomness** aur polite messages aa sakti hain.
# * Agar chahte ho **strictly subtract aur deterministic output** → use:

# ```python
# model_settings = ModelSettings(tool_choice="subtract", temperature=0)
# tool_use_behavior = StopAtTools(stop_at_tool_names=['subtract'])
# ```

# * Ye **har run me exact subtract result** dega, bina extra messages.
# **`tool_choice="subtract"` → LLM mostly subtract tool use karega; `temperature=0` + `StopAtTools=['subtract']` → har run same subtract result, deterministic output.** 


# ! 8. # Agent can use multiple tools at once
# * parallel_tool_calls=True  
# * Use multiple tools simultaneously is ma jo jitne tool ho gy aik sath chaly ka fasts hota hy 


# ! 9. # Agent uses tools one at a time
# * parallel_tool_calls=False  
# * Use tools one by one


# ! 10. # temperature → Creativity control
# * High value = More random / creative output
# * Low value = More focused / deterministic output

# ! 11. # top_p → Vocabulary filtering
# * top_p=0.3 → Sirf top 30% words consider karega
# * Lower value = More controlled and focused wording

# ! 12. # frequency_penalty → Repetition control
# * Higher value = Same words repeat hone se rokta hai
# * Example: 0.5 = Moderate repetition reduction

# ! 13. # presence_penalty → Novelty encouragement
# * Higher value = Model ko naye topics introduce karne push karega
# * Example: 0.3 = Slight encouragement for new ideas
