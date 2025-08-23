
# ! outype_res.py
from agents import Runner
from my_agent.output_agent import output_type_agent
import rich

output_res = Runner.run_sync(
    starting_agent=output_type_agent,
    input="2+2=?"
)

print(output_res.final_output)
print(type(output_res.final_output))
