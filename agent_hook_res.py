from my_agent.agent_hook import agent_hooks
from agents import Runner
import rich
from dataclasses import dataclass


@dataclass
class UserInfo:
    name: str
    uid: int


user_info = UserInfo(name="Bilal", uid=786)

agent_hooks_result = Runner.run_sync(
    starting_agent=agent_hooks,
    input="Please handoff me to refund agent and 2 + 2 = ? and what is my name?",
    context=user_info,   # ✅ yahan context pass kiya
)

rich.print(f"[yellow]===Agent Hook Result===[yellow]\n {agent_hooks_result.final_output}")
