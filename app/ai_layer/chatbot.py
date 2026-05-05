from app.ai_layer.model import model
from app.ai_layer.tools import search_tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver  

agent = create_agent(
    model=model,
    tools=[search_tool],
    checkpointer=InMemorySaver(),
    name="helpfull_assistant",
)

# agent_response = agent.invoke(
#     {"messages": [{"role": "user", "content": "hi my name is bobe"}]},
#     {"configurable": {"thread_id": "1"}},
# )
# print(agent_response)
