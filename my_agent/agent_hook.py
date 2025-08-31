
# ! agent_hook.py

# from agents import Agent
# from my_config.gemini_config import GEMINI_MODEL
# from my_tool.math_tool import plus
# from my_hook.my_agent_hook import MyAgentHook

# agent_hooks= Agent(
#     name="Agent_Hook",
#     instructions="Your are helpfull assistant",
#     model=GEMINI_MODEL,
#     hooks=MyAgentHook(),
#     tools=[plus],
# )

from agents import Agent, handoff
from my_config.gemini_config import GEMINI_MODEL
from my_tool.math_tool import plus
from my_hook.my_agent_hook import MyAgentHook


# Extra agents for handoff
billing_agent = Agent(
    name="Billing_Agent",
    instructions="You are the billing support agent.",
    model=GEMINI_MODEL,
    hooks=MyAgentHook()
)

refund_agent = Agent(
    name="Refund_Agent",
    instructions="You are the refund support agent.",
    model=GEMINI_MODEL,
    hooks=MyAgentHook()
)

# Main agent with hooks, tools and handoffs
agent_hooks = Agent(
    name="Agent_Hook",
    instructions="You are a helpful assistant",
    model=GEMINI_MODEL,
    hooks=MyAgentHook(),
    tools=[plus],
    handoffs=[billing_agent, handoff(refund_agent)],   # ✅ handoffs added
)
