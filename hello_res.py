import asyncio
from agents import Runner
from my_agent.teacher_agents import teacher_agent
from my_agent.general_agent import general_agent

async def main():
    print("\n--- Pattern 1: Proofreader ---")
    result1 = await Runner.run(teacher_agent, "Plz fix this: 'He go to school everyday.'")
    print("User:", "Plz fix this: 'He go to school everyday.'")
    print("Agent:", result1.final_output)

    print("\n--- Pattern 2: Nested Weather Agent ---")
    result2 = await Runner.run(general_agent, "What is the weather like today?")
    print("User:", "What is the weather like today?")
    print("Agent:", result2.final_output)

if __name__ == "__main__":
    asyncio.run(main())
