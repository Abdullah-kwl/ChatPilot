from fastapi import APIRouter
from fastapi import HTTPException
from app.ai_layer.chatbot import agent
from app.api.helper import to_openai_format
from app.api.schemas import Messages, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def root(message: Messages):
    try:
        results = agent.invoke(
        {"messages": [{"role": "user", "content": message.message}]},
        {"configurable": {"thread_id": message.session_id}},
        )
        return {"response": to_openai_format(results["messages"])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))