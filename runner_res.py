

#! runner_res.py

# from my_agent.runner_agent import runner_method_agent
# from agents import Runner
# import rich,asyncio


# ! run
# async def main():
#     runner_method_result =await Runner.run(
#         starting_agent=runner_method_agent,
#         input="Hello"
#     )
#     rich.print("[yellow]=== Result === [yellow]\n", runner_method_result.final_output)


# asyncio.run(main())

# ! run_sync

# runner_method_results = Runner.run_sync(
#         starting_agent=runner_method_agent,
#         input="Hello"
#     )
# rich.print("[yellow]=== Result === [yellow]\n", runner_method_results.final_output)


# ! run_stream
# from openai.types.responses import ResponseTextDeltaEvent
# from agents import ItemHelpers
# async def main():
#     result = Runner.run_streamed(
#         starting_agent=runner_method_agent,
#         input = "Solve this math problem: 2 + 4 "
#     )
    
#     async for event in result.stream_events():
#         # rich.print("[yellow]=== Result === [yellow]\n", result.final_output)
#         # rich.print("[yellow]=== Event === [yellow]\n", event)
#         # rich.print("[red]=== Event Type === [red]", event.type)
#         if event.type == "agent_updated_stream_event":
#             # rich.print("[red]=== Event Type === [red]", event.type)
#             # rich.print("[blue]=== Event New Agent === [blue]", event.new_agent)
#             # rich.print("[green]=== Event Agent Name === [green]", event.new_agent.name)
#             continue
#         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#             # rich.print("[red]=== Event === [red]", event)
#             # rich.print("[red]=== Event Data === [red]", event.data)
#             # rich.print("[red]=== Event Data Delta === [red]", event.data.delta)
#             # rich.print(event.data.delta,end="",flush=True)
#             # rich.print("[red]=== Event Data Delta === [red]", event.data)
#             continue
#         if event.type == "run_item_stream_event":
#             # rich.print("[red]=== Event === [red]", event)
#             # rich.print("[blue]=== Run Item Type ===[blue]", event.item.type)
#             # rich.print("[green]=== Run Item Data ===[green]", event.item)
#             if event.item.type == "handoff_call_item":
#                 # rich.print("[green]=== Event Item ===[green]",event.item)
#                 # rich.print("[blue]=== Event Item Agent ===[blue]",event.item.agent)
#                 # rich.print("[blue]=== Event Item Agent Name ===[blue]",event.item.agent.name)
#                 continue
#             if event.item.type == 'handoff_output_item':
#                 # rich.print("[green]=== Event Item ===[green]",event.item)
#                 # rich.print("[blue]=== Event Item Source Agent ===[blue]",event.item.source_agent)
#                 # rich.print("[yellow]=== Event Item Target Agent ===[yellow]",event.item.target_agent)
#                 # rich.print("[blue]=== Event Item Agent Name ===[blue]",event.item.agent.name)
#                 continue
#             if event.item.type == 'tool_call_item':
#                 # * --- Tool call start ---
#                 # print("[green] === Tool was called === [green]")
#                 # rich.print("[yellow]Tool was called:[/yellow]", event.item.tool.name)
#                 continue
#             if event.item.type == "tool_call_output_item":
#                 # * --- Tool output ---
#                 # rich.print("[green]=== Event Item ===[green]",event.item)
#                 # rich.print("[blue]=== Event Item Output ===[blue]",event.item.output)
#                 continue
#             if event.item.type == "message_output_item":
#                 print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
                

# asyncio.run(main())


# ! === Final Streaming Working ===
# ! runner_res.py
from my_agent.runner_agent import runner_method_agent
from agents import Runner, ItemHelpers
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
import rich

# ! run_stream
async def main():
    # Start the streamed run
    result = Runner.run_streamed(
        starting_agent=runner_method_agent,
        input="Solve this math problem: 2 + 4"
    )
    
    async for event in result.stream_events():
        # --- Raw response event (token by token) ---
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            # Ignored in this example
            # rich.print("[red]Raw response event:[/red]", event.data.delta)
            continue

        # --- Agent updated (handoff or agent change) ---
        elif event.type == "agent_updated_stream_event":
            # rich.print("[red]Agent updated event detected[/red]")
            # rich.print("[blue]New Agent:[/blue]", event.new_agent.name)
            continue

        # --- Run item events (tool calls, tool outputs, messages) ---
        elif event.type == "run_item_stream_event":
            item_type = event.item.type

            # Handoff call started
            if item_type == "handoff_call_item":
                # rich.print("[green]Handoff call started[/green]")
                # rich.print("[blue]Handoff Agent:[/blue]", event.item.agent.name)
                continue

            # Handoff output produced
            elif item_type == 'handoff_output_item':
                # rich.print("[green]Handoff output produced[/green]")
                # rich.print("[blue]Source Agent:[/blue]", event.item.source_agent.name)
                # rich.print("[yellow]Target Agent:[/yellow]", event.item.target_agent.name)
                continue

            # Tool was called
            elif item_type == 'tool_call_item':
                # * --- Tool call start ---
                # rich.print("[yellow]Tool called:[/yellow]", event.item.tool.name)
                continue

            # Tool output
            elif item_type == "tool_call_output_item":
                # * --- Tool output ---
                # rich.print("[green]Tool output detected[/green]")
                # rich.print("[blue]Output:[/blue]", event.item.output)
                continue

            # Agent's message output
            elif item_type == "message_output_item":
                # Display the message output from agent
                msg = ItemHelpers.text_message_output(event.item)
                print(f"-- Message output:\n{msg}")
                continue

            else:
                # Ignore other run item types
                continue

    # Run finished
    print("=== Run complete ===")


# Run async main
if __name__ == "__main__":
    asyncio.run(main())


# * **Sync = ruk ke wait karna (dusra kaam band ho jata hai)**
# * **Async = wait karna lekin side me dusre kaam bhi chal sakte hain**

#  **Runner.run\_sync / run\_async** ka workflow samjhata hai 👇

# ---

### 🔄 Workflow ka simple breakdown:

# 1. **Agent start hota hai** (tum jo `starting_agent` dete ho us se).

# 2. **Loop chalta hai**:

#    * Agent ko **input** diya jata hai.
#    * Agar **final output** mil gaya (jo `agent.output_type` se match karta hai) → loop khatam ✅
#    * Agar **handoff** hua (dusre agent ko kaam de diya) → loop fir se us naye agent ke sath start hota hai 🔄
#    * Agar **tool call** kiya gaya → tool run hota hai, phir agent ko dobara chalaya jata hai.

# 3. **Exceptions aa sakti hain**:

#    * Agar **max\_turns** limit cross ho gayi → `MaxTurnsExceeded` error ❌
#    * Agar **guardrail tripwire** trigger hua → `GuardrailTripwireTriggered` error ❌

# 4. **Note:** Sirf pehle agent ke input guardrails run hote hain.

# ---

# ### 🔑 Args (simple language me)

# * **starting\_agent** → sabse pehle jo agent run hoga.
# * **input** → user ka message ya input list.
# * **context** → shared data jo sab agents access karte hain.
# * **max\_turns** → loop kitni dafa chalne ki limit.
# * **hooks** → agar tumhe har step par callbacks chahiye (debugging/logging ke liye).
# * **run\_config** → global settings for run.
# * **previous\_response\_id** → agar OpenAI ka Responses API use ho raha hai aur tum last response se continue karna chahte ho.
# * **conversation\_id** → agar tum OpenAI ka conversation state use karna chahte ho, taki pura history sab agents ke paas rahe.

# ---


# ! `Runner.run_sync(...)`
# ye jo text hai, wo **`Runner.run_sync(...)` function** ka explanation hai (yaani synchronous workflow chalana). isme bataya gaya hai:

# ### 🔹 Kya karta hai?

# * ek **agent workflow ko sync mode** me chalata hai (step by step).
# * jab tak **final output** nahi milta, tab tak loop chalta rehta hai.

# ### 🔹 Loop kaise chalta hai?

# 1. agent ko **input** diya jata hai.
# 2. agar **final output** mil jaye → loop band.
# 3. agar **handoff** ho jaye → naya agent start karke loop continue.
# 4. agar agent ne **tools use kiye** → tools run hote hain aur phir loop continue.

# ### 🔹 Exception kab aayega?

# 1. agar **max\_turns exceed** ho gaye → `MaxTurnsExceeded`.
# 2. agar **guardrail tripwire** trigger ho gaya → `GuardrailTripwireTriggered`.

# ### 🔹 Args (parameters) ka matlab:

# * **starting\_agent** → pehla agent jo start karega.
# * **input** → user ka input (string ya list).
# * **context** → agent ka context.
# * **max\_turns** → maximum steps (safety ke liye).
# * **hooks** → lifecycle events handle karne ke liye.
# * **run\_config** → global settings.
# * **previous\_response\_id** / **conversation\_id** → agar pehle se conversation chal rahi hai.

# ### 🔹 Return kya milta hai?

# ek **run result object** jisme:

# * sab inputs,
# * guardrail results,
# * aur final output hota hai.

# ---

# 👉 Simple me:
# ye function ek agent workflow ko **sync tarike se chalata hai** → har step me check karta hai output aya, handoff hua, ya tool call hua. agar output mil gaya to ruk jata hai. agar error hua to exception deta hai.

# ---

