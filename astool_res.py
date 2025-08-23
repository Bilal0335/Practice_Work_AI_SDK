


# ! astool_res.py
# from agents import Runner
# from my_agent.astool_agent import sec_agent
# import rich

# output_res = Runner.run_sync(
#     starting_agent=sec_agent,
#     input="2+2=?"
# )

# rich.print(output_res.final_output)


# ! Travel Planner Result

# ------------------ Runner ------------------
from agents import Runner
from rich.console import Console
from rich.text import Text
from my_agent.astool_agent import orchestrator_agent
import asyncio

console = Console()

async def main():
    user_input = "Plan my trip to Dubai"

    console.print(f"[bold yellow]User Request:[/bold yellow] {user_input}\n")

    result = await Runner.run(orchestrator_agent, input=user_input)

    console.print("[bold green]=== Final Trip Plan ===[/bold green]\n")

    # Simple colorful output
    text = Text(result.final_output, style="cyan")
    console.print(text)


if __name__ == "__main__":
    asyncio.run(main())

