

# ! my_agent_hook.py
from agents import AgentHooks, RunContextWrapper, TContext, Agent, Tool
import rich
from typing import Any


class MyAgentHook(AgentHooks):
    async def on_start(self, context: RunContextWrapper[TContext], agent: Agent) -> None:
        """Agent start hone se pehle chalega"""
        rich.print(f"[green]Start Agent Hook[/green] - Agent Name: {agent.name}")

        # Agar context me custom data hai
        if context.context:
            rich.print(f"[blue]Custom Context Data:[/blue] {context.context}")

    async def on_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        output: Any,
    ) -> None:
        """Agent ka final output milne ke baad chalega"""
        rich.print(f"[red]End Agent Hook[/red] - Agent Name: {agent.name}")
        rich.print(f"[yellow]Final Output:[/yellow] {output}")

    async def on_tool_start(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
    ) -> None:
        """Tool call hone se just pehle chalega"""
        rich.print(f"[cyan]Tool Start Hook[/cyan] - Agent: {agent.name}, Tool: {tool.name}")

    async def on_tool_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
        result: str,
    ) -> None:
        """Tool call hone ke baad chalega"""
        rich.print(f"[magenta]Tool End Hook[/magenta] - Agent: {agent.name}, Tool: {tool.name}")
        rich.print(f"[bold green]Tool Result:[/bold green] {result}")

    async def on_handoff(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        source: Agent,
    ) -> None:
        """Jab ek agent dusre agent ko handoff karega"""
        rich.print(f"[orange3]Handoff Hook[/orange3] - From: {source.name} -> To: {agent.name}")
