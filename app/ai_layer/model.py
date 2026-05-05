from langchain_groq import ChatGroq
from app.utils.config import secrets, config

model = ChatGroq(model=config.model, groq_api_key=secrets.GROQ_API_KEY)

# results =model.invoke("Hello, how are you?")
# print(results)