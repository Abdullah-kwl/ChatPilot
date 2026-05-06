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