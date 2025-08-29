

# # ! customize_handoff_res.py

# from agents import Runner
# from my_agent.customize_handoff_agen import assistant_agent
# from rich import print

# # Run the agent
# handoff_result = Runner.run_sync(
#     starting_agent=assistant_agent,
#     input="what is weather in karachi ? and 2 + 2 = ?? deatil",
#     context={
#         "name":"Bilal",
#         "role":"Student",
#         "age":20
#     }
# )

# # Print results with rich colors and simple separators
# print("\n[bold green]==== Handoff Result ====[/bold green]")
# print(f"[cyan]Last Agent:[/cyan] [yellow]{handoff_result._last_agent.name}[/yellow]")
# print(f"[cyan]Final Output:[/cyan] [magenta]{handoff_result.final_output}[/magenta]")
# print("[bold green]========================[/bold green]\n")



# ! customize_handoff_res.py
# from agents import Runner
# from my_agent.customize_handoff_agen import assistant_agent
# from rich import print

# Run the main agent
# handoff_result = Runner.run_sync(
#     starting_agent=assistant_agent,
#     input="What is the weather in Karachi? And 2 + 2 = ?? Detail",
#     context={
#         "name": "Bilal",
#         "role": "Student",
#         "age": 20
#     }
# )

# # Print results
# print("\n[bold green]==== Handoff Result ====[/bold green]")
# print(f"[cyan]Last Agent:[/cyan] [yellow]{handoff_result._last_agent.name}[/yellow]")
# print(f"[cyan]Final Output:[/cyan] [magenta]{handoff_result.final_output}[/magenta]")
# print("[bold green]========================[/bold green]\n")









# ! customize_handoff_res.py
from agents import Runner
from my_agent.customize_handoff_agen import assistant_agent
from rich import print

# Run the main agent
handoff_result = Runner.run_sync(
    starting_agent=assistant_agent,
    input="what is weather in Lahore. Also solve 2 + 2 in detail.",
    context={
        "name": "Bilal",
        "role": "Student",
        "age": 10
    }
)

# Print results
print("\n[bold green]==== Handoff Result ====[/bold green]")
print(f"[cyan]Last Agent:[/cyan] [yellow]{handoff_result._last_agent.name}[/yellow]")
print(f"[cyan]Final Output:[/cyan] [magenta]{handoff_result.final_output}[/magenta]")
print("[bold green]========================[/bold green]\n")
