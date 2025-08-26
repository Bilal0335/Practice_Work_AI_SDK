# ! clone_shared_demo.py
from agents import Agent, Runner, function_tool
from my_tool.math_tool import calculate_area

# --- Base agent with one tool ---
original_agent = Agent(
    name="OriginalAgent",
    tools=[calculate_area],
    instructions="You are a helpful assistant."
)

# --- Clone WITHOUT giving new tools list (SHARED reference) ---
shared_clone = original_agent.clone(
    name="SharedClone",
    instructions="You are a creative assistant."
)

# --- Add a new tool to original ---
@function_tool
def new_tool() -> str:
    return "I'm a new tool!"

original_agent.tools.append(new_tool)

# Both original and shared_clone now have 2 tools (shared list)
print("🔹 Original tools:", len(original_agent.tools))   # 2
print("🔹 Shared clone tools:", len(shared_clone.tools)) # 2

# --- Independent clone (NEW list of tools) ---
independent_clone = original_agent.clone(
    name="IndependentClone",
    tools=[calculate_area],   # Fresh list
    instructions="You are an independent assistant."
)

# Add the same tool again in original
original_agent.tools.append(new_tool)

# Independent clone stays unaffected
print("🔹 Original tools after adding again:", len(original_agent.tools))       # 3
print("🔹 Independent clone tools:", len(independent_clone.tools))             # 1
