
# ! my_run_hook.py
from agents import RunHooks, TContext, RunContextWrapper, Agent, Tool
from typing import Any
import rich

class MyRunHook(RunHooks):
    async def on_agent_start(self, context: RunContextWrapper[TContext], agent: Agent) -> None:
        """Agent start hone se pehle chalega (per run)."""
        rich.print(f"[green]Start RunHook[/green] - Agent Name: {agent.name}")
        if context.context:
            rich.print(f"[blue]Custom Context Data (RunHook):[/blue] {context.context}")

    async def on_agent_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        output: Any,
    ) -> None:
        """Jab agent final output deta hai."""
        rich.print(f"[red]End RunHook[/red] - Agent Name: {agent.name}")
        rich.print(f"[yellow]Final Output (RunHook):[/yellow] {output}")

    async def on_handoff(
        self,
        context: RunContextWrapper[TContext],
        from_agent: Agent,
        to_agent: Agent,
    ) -> None:
        """Jab ek agent dusre agent ko handoff karega."""
        rich.print(f"[orange3]RunHook Handoff[/orange3] - From: {from_agent.name} -> To: {to_agent.name}")

    async def on_tool_start(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
    ) -> None:
        """Tool call hone se pehle chalega."""
        rich.print(f"[cyan]RunHook Tool Start[/cyan] - Agent: {agent.name}, Tool: {tool.name}")

    async def on_tool_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
        result: str,
    ) -> None:
        """Tool call complete hone ke baad chalega."""
        rich.print(f"[magenta]RunHook Tool End[/magenta] - Agent: {agent.name}, Tool: {tool.name}")
        rich.print(f"[bold green]RunHook Tool Result:[/bold green] {result}")
