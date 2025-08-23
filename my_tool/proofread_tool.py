from agents import Runner, function_tool
from my_agent.proofreader_agent import proofreader

@function_tool
async def proofread_text(text: str) -> str:
    """Fix grammar and punctuation; return only corrected text."""
    try:
        result = await Runner.run(
            proofreader,
            text,
            max_turns=3,
            timeout=10,
        )
        return str(result.final_output).strip()
    except Exception as e:
        return f"[Proofreader error: {e}]"
