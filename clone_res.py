

# ! clone_res.py

# from agents import Runner
# from my_agent.clone_agent import poet, scientist, weather_agent, math_agent
# from rich import print

# --- USER QUERY EXAMPLES ---
# For poetry / science:
# query = "What is love?"

# For math tool:
# query = "Calculate area of rectangle with length 5 and width 10"

# For weather tool:
# query = "What is the weather in London?"

# For normal math:
# query = "What is 25 - 12?"

# query = "What is love?"

# # --- Run Agents ---
# poet_res = Runner.run_sync(
#     starting_agent=poet,
#     input=query
# )

# scientist_res = Runner.run_sync(
#     starting_agent=scientist,
#     input="What is chemistry and formula water."
# )

# weather_res = Runner.run_sync(
#     starting_agent=weather_agent,
#     input="What is the weather in New York?"
# )

# math_res = Runner.run_sync(
#     starting_agent=math_agent,
#     input="Calculate area of rectangle with length 7 and width 3"
# )

# # --- Print Results ---
# print("\n[bold cyan]=== Poet Says ===[/bold cyan]")
# print(f"[italic yellow]{poet_res.final_output}[/italic yellow]")

# print("\n[bold green]=== Scientist Says ===[/bold green]")
# print(f"[italic white]{scientist_res.final_output}[/italic white]")

# print("\n[bold blue]=== Weather Assistant Says ===[/bold blue]")
# print(f"[italic magenta]{weather_res.final_output}[/italic magenta]")

# print("\n[bold magenta]=== Math Assistant Says ===[/bold magenta]")
# print(f"[italic cyan]{math_res.final_output}[/italic cyan]")


# ! pratice work
# from agents import Runner
# from my_agent.clone_agent import multiple_agents
# from rich import print

# User query
# query = "Tell me about artificial intelligence."

# Color mapping for agents
# agent_colors = {
#     "Weather": "blue",
#     "Math": "magenta",
#     "Creative": "yellow",
#     "Precise": "green",
# }

# Loop through each agent and run query
# for name, agent in multiple_agents.items():
#     res = Runner.run_sync(
#         starting_agent=agent,
#         input=query
#     )
#     color = agent_colors.get(name, "white")
#     print(f"\n[bold {color}]=== {name} Agent Says ===[/bold {color}]")
#     print(f"[italic {color}]{res.final_output[:200]}...[/italic {color}]")


# ! clone_res.py

# from agents import Runner
# from my_agent.clone_agent import poet, scientist, weather_agent, math_agent
# from rich import print

# query = "What is love?"

# # Dictionary of all clones
# agents = {
#     "Poet": poet,
#     "Scientist": scientist,
#     "Weather Assistant": weather_agent,
#     "Math Assistant": math_agent,
# }

# # Color mapping for agents
# agent_colors = {
#     "Poet": "yellow",
#     "Scientist": "green",
#     "Weather Assistant": "blue",
#     "Math Assistant": "magenta",
# }

# # Loop through each agent and run query
# for name, agent in agents.items():
#     res = Runner.run_sync(
#         starting_agent=agent,
#         input=query
#     )

#     color = agent_colors.get(name, "white")  # default white if not found

#     print(f"\n[bold {color}]=== {name} Says ===[/bold {color}]")
#     print(f"[italic {color}]{res.final_output}[/italic {color}]")


# ! # Demonstrate shared references
# ! clone_res.py
from agents import Runner
from my_agent.clone_agent import original_agent, clone_agent, shared_clone, independent_clone
from my_tool.math_tool import new_tool


print("=== Running OriginalAgent ===")
res1 = Runner.run_sync(original_agent, "Calculate the area of a rectangle 5x6.")
print(res1.final_output)

print("=== Running CloneAgent ===")
res2 = Runner.run_sync(clone_agent, "Calculate the area of a rectangle 7x3.")
print(res2.final_output)


# ======================================================
# DEMO SECTION
# ======================================================
print("\n=== DEMO: Shared vs Independent Clone ===")

# Add new tool dynamically into original
original_agent.tools.append(new_tool)

print("🔹 Tools count (Original):", len(original_agent.tools))
print("🔹 Tools count (SharedClone):", len(shared_clone.tools))
print("🔹 Tools count (IndependentClone):", len(independent_clone.tools))

# Test run with shared clone (it sees new_tool)
res3 = Runner.run_sync(shared_clone, "Use the new tool please.")
print("SharedClone says:", res3.final_output)

# Test run with independent clone (doesn't have new_tool)
res4 = Runner.run_sync(independent_clone, "Use the new tool please.")
print("IndependentClone says:", res4.final_output)
