

# ! guardrails_res.py

import rich
from my_agent.guardrails_agent import guardrail_agent
from my_agent.hotel_agent_guard import hotel_agent_guardrail
from agents import Runner,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered


try:
    guardrails_result = Runner.run_sync(
        starting_agent=hotel_agent_guardrail,
        input="how much tax deducted on single room in Hotel Sannata's?"
    )
    
    rich.print(guardrails_result.final_output)

except InputGuardrailTripwireTriggered as e:
    rich.print(f"[red]Tripwire Triggered Input:[/red] {e}")

except OutputGuardrailTripwireTriggered as e:
    rich.print(f"[red]Tripwire Triggered Output:[/red] {e}")


# guardrails_result = Runner.run_sync(
#     starting_agent=guardrail_agent,
#     input="how many room available in Hotel Sannata's?"
# )



