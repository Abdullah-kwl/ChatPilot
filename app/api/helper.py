from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def to_openai_format(messages):
    formatted = []

    for msg in messages:
        if isinstance(msg, HumanMessage):
            formatted.append({
                "role": "user",
                "content": msg.content
            })

        elif isinstance(msg, AIMessage):
            formatted.append({
                "role": "assistant",
                "content": msg.content
            })

        elif isinstance(msg, SystemMessage):
            formatted.append({
                "role": "system",
                "content": msg.content
            })

        # ToolMessage → ignored

    return formatted