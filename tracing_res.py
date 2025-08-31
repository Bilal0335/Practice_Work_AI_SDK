

# ! tracing_res.py

from my_agent.tracing_agent import tracing_agents
from agents import Runner,trace
import rich

# tracing_result = Runner.run_sync(
#     starting_agent=tracing_agents,
#     input="Hello"
# )

# rich.print(f"[yellow]===Tracing Result===[yellow]\n {tracing_result.final_output}")


# * Wrap in a custom trace
with trace("Bilal workflow"):
    tracing_result = Runner.run_sync(
        starting_agent=tracing_agents,
        input="What is my name"
    )

rich.print(f"[yellow]===Tracing Result===[yellow]\n {tracing_result.final_output}")