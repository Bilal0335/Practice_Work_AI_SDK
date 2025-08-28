

# ! handoff_res.py
# from agents import Runner
# from my_agent.handoff_agent import assistant_agent
# from rich import print

# # Run the agent
# handoff_result = Runner.run_sync(
#     starting_agent=assistant_agent,
#     input="what is a fundamentao of english?"
# )

# # Print results with rich colors and simple separators
# print("\n[bold green]==== Handoff Result ====[/bold green]")
# print(f"[cyan]Last Agent:[/cyan] [yellow]{handoff_result._last_agent.name}[/yellow]")
# print(f"[cyan]Final Output:[/cyan] [magenta]{handoff_result.final_output}[/magenta]")
# print("[bold green]========================[/bold green]\n")


# ! pratice work
# from agents import Runner
# from my_agent.handoff_agent import triage_agent
# from rich import print

# handoff_result =  Runner.run_sync(
#     triage_agent,
#     "I need to check refund status."
#     )
# # print(handoff_result.final_output)  # Specialist agent ka reply
# # Print results with rich colors and simple separators
# print("\n[bold green]==== Handoff Result ====[/bold green]")
# print(f"[cyan]Last Agent:[/cyan] [yellow]{handoff_result._last_agent.name}[/yellow]")
# print(f"[cyan]Final Output:[/cyan] [magenta]{handoff_result.final_output}[/magenta]")
# print("[bold green]========================[/bold green]\n")

# ! Pratice work
# from agents import Runner
# from my_agent.handoff_agent import triage_agent
# from rich import print

# # --- User query ---
# user_query = "I need a refund for my last order"

# # --- Run the agent ---
# result = Runner.run_sync(triage_agent, user_query)

# # --- Rich colored output ---
# print("\n[bold green]==== Handoff Result ====[/bold green]")
# print(f"[cyan]User Query:[/cyan] [yellow]{user_query}[/yellow]")
# print(f"[cyan]Last Agent Who Answered:[/cyan] [magenta]{result.last_agent.name}[/magenta]")
# print(f"[cyan]Final Output:[/cyan] [white]{result.final_output}[/white]")

# # --- Check if handoff occurred ---
# print("\n[bold yellow]Handoff Items (proof of handoff):[/bold yellow]")
# for item in result.new_items:
#     print(f"[yellow]{type(item).__name__}: {item}[/yellow]")

# print("[bold green]========================[/bold green]\n")

# ---

# ### 1️⃣ Key points

# Aapka output me teen main items dikh rahe hain:

# 1. **`HandoffCallItem`**
# 2. **`HandoffOutputItem`**
# 3. **`MessageOutputItem`**

# Ye **proof hai ke handoff process hua** aur query specialist agent ne handle ki.

# ---

# ### 2️⃣ `HandoffCallItem`

# * Matlab: **Triage agent ne Refund agent ko handoff kiya**.
# * Key info:

#   * `agent=Agent(name='Triage agent')` → ye agent ne handoff initiate kiya
#   * `tool_name='transfer_to_refund_agent'` → ye handoff tool ka name hai
#   * `target_agent=Refund agent` → ye agent jisko handoff hua

# **Interpretation:**

# ```
# Triage agent ne Refund agent ko call kiya via handoff tool
# ```

# ---

# ### 3️⃣ `HandoffOutputItem`

# * Matlab: **Refund agent ne response generate kiya**.
# * Key info:

#   * `source_agent=Agent(name='Triage agent')` → jo agent ne handoff call kiya
#   * `target_agent=Agent(name='Refund agent')` → jo agent ne actually answer diya
#   * `raw_item={'call_id': ..., 'output': '{"assistant": "Refund agent"}'}` → raw response from handoff

# **Interpretation:**

# ```
# Refund agent ne user query ka answer diya aur handoff complete hua
# ```

# ---

# ### 4️⃣ `MessageOutputItem`

# * Matlab: **final user-facing message** jo Refund agent ne generate kiya.
# * Key info:

#   * `text="I'd be happy to help you with your refund. Can you please provide me with more details ..."` → actual assistant ka reply
#   * `role='assistant'` → ye assistant ka message hai

# **Interpretation:**

# ```
# User ko jo reply mila, wo MessageOutputItem me store hai
# ```

# ---

# ### 5️⃣ Simple mental model

# ```
# User Question → Triage agent
#     ↓ HandoffCallItem
# Refund agent responds → HandoffOutputItem
#     ↓ Final output
# User sees message → MessageOutputItem
# ```

# * `HandoffCallItem` = handoff start
# * `HandoffOutputItem` = handoff response
# * `MessageOutputItem` = final answer jo user dekhe

# ---

# ### ✅ Summary

# * `result.new_items` me ye teen types se **proof milta hai ke handoff hua aur kaun respond kiya**.
# * Aap **debugging aur logging ke liye** use kar sakte ho: kaun agent ne query receive ki, kaunne respond kiya.
# * `result.last_agent.name` → direct last agent ka naam, jo final output generate kiya.

# ---

# Agar chaho, main ye output **rich colors me nicely print karne wala mini script** bana doon jo:

# 1. Handoff call show kare
# 2. Handoff output show kare
# 3. Final message show kare


# ! pratice 
# ! handoff_res.py
import asyncio
from agents import Runner
from my_agent.handoff_agent import router
from rich import print

async def main():
    # ---- Turn 1: user asks about running → should handoff to Fitness Coach
    r1 = await Runner.run(router, "I want to run a 5Km in 8 weeks. Can you help?")

    print("\n[bold green]==== Turn 1 ====[/bold green]")
    print(f"[cyan]User Query:[/cyan] [yellow]I want to run a 5Km in 8 weeks. Can you help?[/yellow]")
    print(f"[cyan]Specialist Agent:[/cyan] [magenta]{r1.last_agent.name}[/magenta]")
    print(f"[white]{r1.final_output}[/white]")
    print("[bold green]========================[/bold green]\n")

    # Grab the specialist that actually replied (Fitness Coach)
    specialist = r1.last_agent

    # ---- Turn 2: continue with same specialist
    t2_input = r1.to_input_list() + [
        {"role": "user", "content": "Right now I can jog about 2 km, 3 days per week."}
    ]
    r2 = await Runner.run(specialist, t2_input)

    print("\n[bold green]==== Turn 2 ====[/bold green]")
    print(f"[cyan]User Input:[/cyan] [yellow]Right now I can jog about 2 km, 3 days per week.[/yellow]")
    print(f"[cyan]Specialist Agent:[/cyan] [magenta]{r2.last_agent.name}[/magenta]")
    print(f"[white]{r2.final_output}[/white]")
    print("[bold green]========================[/bold green]\n")

    # ---- Turn 3: another follow-up; same specialist
    t3_input = r2.to_input_list() + [
        {"role": "user", "content": "Nice. What should I eat on training days?"}
    ]
    r3 = await Runner.run(specialist, t3_input)

    print("\n[bold green]==== Turn 3 ====[/bold green]")
    print(f"[cyan]User Input:[/cyan] [yellow]Nice. What should I eat on training days?[/yellow]")
    print(f"[cyan]Specialist Agent:[/cyan] [magenta]{r3.last_agent.name}[/magenta]")
    print(f"[white]{r3.final_output}[/white]")
    print("[bold green]========================[/bold green]\n")


if __name__ == "__main__":
    asyncio.run(main())
