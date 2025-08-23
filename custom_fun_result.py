
from agents import Runner
from my_agent.custom_fun_agent import cust_fun_agents
from rich.console import Console

console = Console()

custum_res = Runner.run_sync(
    starting_agent=cust_fun_agents,
    input="subtract 10 and 5",
    context={"name":"Bilal","age":20,'role':"student"}
)

console.print("\n" + "=" * 30, style="red")
console.print("custom function tools", style="bright_yellow")
console.print("=" * 30, style="red")

console.print(f"Final Output: [bold green]{custum_res.final_output}[/bold green]")
console.print("=" * 30, style="red")
