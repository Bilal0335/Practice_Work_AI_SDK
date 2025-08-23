

# ! tool_res.py
# from agents import Runner
# from my_agent.tool_agent import tools_agent
# from rich import print

# tool_result = Runner.run_sync(
#     starting_agent=tools_agent,
#     input="2+2=? jo answer ay us sy multiple kro 10 sy aur jo be answer ay us minus kr dou 30 sy "
# )

# print("[bold magenta]=== Final Output ===[/bold magenta]\n", tool_result.final_output)


# ! tool_res.py

from agents import Runner
from my_agent.tool_agent import tools_agent
from rich import print

# ---- Math Example ----
math_result = Runner.run_sync(
    starting_agent=tools_agent,
    input="First do 12+8, then multiply the result by 10, then subtract 30."
)

print("[bold magenta]=== Math Output ===[/bold magenta]")
print(math_result.final_output)
print("Operation:", math_result.final_output.operation)
print("Input Values:", math_result.final_output.input_values)
print("Result:", math_result.final_output.result)

# ---- Weather Example ----
# weather_result = Runner.run_sync(
#     starting_agent=tools_agent,
#     input="Mujhe SF ka weather batao. Latitude 37.77, Longitude -122.42"
# )



# print("\n[bold cyan]=== Weather Output ===[/bold cyan]")
# print(weather_result.final_output)
# print("Operation:", weather_result.final_output.operation)
# print("Result:", weather_result.final_output.result)



