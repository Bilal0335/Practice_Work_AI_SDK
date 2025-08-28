
# ! guardrails_input_fun.py
from agents import RunContextWrapper, GuardrailFunctionOutput, input_guardrail, Runner,Agent,TResponseInputItem
import rich
from my_agent.guardrails_agent import guardrail_agent

@input_guardrail
async def guardrail_input_fun(ctx: RunContextWrapper[None], agent:Agent, input:str|list[TResponseInputItem]) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input=input, context=ctx.context)
    rich.print("Agent -->",agent)
    rich.print("Agent Name -->",agent.name)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_hotel_sanata_query
    )
