
# ! guardrails_input_fun.py
from agents import RunContextWrapper, GuardrailFunctionOutput, input_guardrail, Runner
from my_agent.guardrails_agent import guardrail_agent

@input_guardrail
async def guardrail_input_fun(ctx: RunContextWrapper, agent, input):
    result = await Runner.run(guardrail_agent, input=input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_hotel_sanata_query
    )
