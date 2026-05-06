from fastapi import APIRouter
from app.api.schemas import Messages, ChatResponse
from app.ai_layer.chatbot import agent
from app.api.helper import to_openai_format

router = APIRouter()


@router.post("/chat")
async def root(message: Messages, response_model=ChatResponse):
    try:
        results = agent.invoke(
        {"messages": [{"role": "user", "content": message.message}]},
        {"configurable": {"thread_id": message.session_id}},
        )
        return {"response": to_openai_format(results["messages"])}
    except Exception as e:
        return {"error": str(e)}