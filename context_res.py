from agents import Runner
import rich
from my_agent.context_agent import context_agents
from my_data_type.context_data import userData

context_result = Runner.run_sync(
    starting_agent=context_agents,
    input="Hello",
    context=userData(
        name="akmal",
        age=14,
        role="Student"
    )
)

rich.print(context_result.final_output)
