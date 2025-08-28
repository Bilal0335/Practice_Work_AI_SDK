

# ! guardrails_output_fun.py
from agents import Runner,output_guardrail,GuardrailFunctionOutput,RunContextWrapper,Agent
from my_agent.guardrails_agent import guardrail_agent


@output_guardrail
async def guardrail_output_fun(ctx:RunContextWrapper[None],agent:Agent,output) -> GuardrailFunctionOutput:
    result = await Runner.run(
        guardrail_agent,
        input=output,
        context=ctx.context
    )
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_hotel_sanata_account_or_text_query
    )