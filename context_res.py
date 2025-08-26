# from agents import Runner
# import rich
# from my_agent.context_agent import context_agents
# from my_data_type.context_data import userData


# user1 = userData(
#         name="akmal",
#         age=14,
#         role="Student"
#     )

# context_result = Runner.run_sync(
#     starting_agent=context_agents,
#     input="Hello",
#     context=user1
# )

# rich.print(context_result.final_output)



# from agents import Runner
# from my_data_type.context_data import UserData
# from my_agent.context_agent import context_agents
# import rich

# user1 = UserData(
#     name="Ali",
#     age=16,
#     role="Student",
#     favorite_subject="Math",
#     study_hours=4
# )

# result = Runner.run_sync(
#     starting_agent=context_agents,
#     input="What plan do you recommend for my teaching?",
#     context=user1
# )

# rich.print(result.final_output)

from agents import Runner
from my_data_type.context_data import UserData
from my_agent.context_agent import context_agents
import rich

# Create user context
user1 = UserData(
    name="Ali",
    age=16,
    role="Student",
    favorite_subject="Math",
    study_hours=4
)

# Run agent with context
result = Runner.run_sync(
    starting_agent=context_agents,
    input="How many hours should my child spend studying?",
    context=user1
)

rich.print(result.final_output)

