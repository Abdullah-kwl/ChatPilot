from pydantic import BaseModel

class Messages(BaseModel):
    message : str
    session_id : str

class ChatResponse(BaseModel):
    response : list[dict]