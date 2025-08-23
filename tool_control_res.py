
# ! tool_control_res.py

from agents import Runner
from my_agent.tool_control_agent import tool_control_agents,math_tutor,creative_writer,focused_agent
from rich.console import Console

console = Console()

# * tool_control_result
# tool_control_result = Runner.run_sync(
#     starting_agent=tool_control_agents,
#     input="2 + 2 ko add karo aur phir subtract 1",
#     # input="2 + 2 = ? jo be answer ay ka us ko multuply kr dou 10 aur jo be answer ay ka us ma minus kr dou 10 ko ",
#     # input="hello", modelseeting ma required wala 
#     # input="12 + 4 = ??",
#     max_turns=2
# )

# # Simple output with colors and === line
# console.print("\n" + "=" * 30, style="magenta")
# console.print("Tool Control Result", style="cyan")
# console.print("=" * 30, style="magenta")

# console.print(f"Final Output: [bold yellow]{tool_control_result.final_output}[/bold yellow]")
# console.print("=" * 30, style="blue")

# * MaxTurnsExceeded
# async def main():
#     try:
#         res = await Runner.run(tool_control_agents, "12 + 4 = ??", max_turns=2)
#         print(res.new_items)
#     except MaxTurnsExceeded as e:
#         print(f"Max turns exceeded: {e}")

# if __name__ == "__main__":
#     asyncio.run(main())


# * Math Tutor Result
# math_res = Runner.run_sync(
#     starting_agent=math_tutor, 
#     input="Solve: 2x + 5 = 13"
# )

# console.print("\n" + "=" * 30, style="green")
# console.print("Math Tutor Result", style="bright_cyan")
# console.print("=" * 30, style="green")

# console.print(f"Final Output: [bold yellow]{math_res.final_output}[/bold yellow]")
# console.print("=" * 30, style="green")


# * # Creative Writer Result
# cretive_res = Runner.run_sync(
#     creative_writer, 
#     "Write a short story about a robot learning to paint"
# )

# console.print("\n" + "=" * 30, style="blue")
# console.print("Creative Writer Result", style="bright_magenta")
# console.print("=" * 30, style="blue")

# console.print(f"Final Output: [bold white]{cretive_res.final_output}[/bold white]")
# console.print("=" * 30, style="blue")


# *Focused Agent Result
focused_res = Runner.run_sync(
    starting_agent=focused_agent,
    input="Write a motivational message about learning new skills"
)

console.print("\n" + "=" * 30, style="red")
console.print("Focused Agent Result", style="bright_yellow")
console.print("=" * 30, style="red")

console.print(f"Final Output: [bold green]{focused_res.final_output}[/bold green]")
console.print("=" * 30, style="red")
