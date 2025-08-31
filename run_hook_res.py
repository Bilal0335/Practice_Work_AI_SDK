
# ! run_hook_res.py
from my_agent.run_hook import run_hooks_assistant
from agents import Runner
import rich
from my_hook.my_run_hook import MyRunHook
from dataclasses import dataclass


@dataclass
class UserInfo:
    name: str
    uid: int


user_info = UserInfo(name="Bilal", uid=786)

run_hooks_result = Runner.run_sync(
    starting_agent=run_hooks_assistant,
    input="hi, 2 + 2 = ? and I have a billing issue, please transfer me to billing agent",
    context=user_info,   # ✅ yahan context pass kiya,
    hooks=MyRunHook()
 
)

rich.print(f"[yellow]===Run Result===[yellow]\n {run_hooks_result.final_output}")

