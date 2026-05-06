import streamlit as st
import requests
import uuid

# CONFIG
st.set_page_config(
    page_title="ChatPilot",
    page_icon="🤖",
    layout="centered",
)

FASTAPI_URL = "http://localhost:8000/api/v1/chat"


# SESSION STATE
def init_session():
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "messages" not in st.session_state:
        st.session_state.messages = []


init_session()


# BACKEND CALL
def get_assistant_reply(message: str, session_id: str) -> str:
    try:
        response = requests.post(
            FASTAPI_URL,
            json={
                "message": message,
                "session_id": session_id,
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return f"⚠️ Backend error: {data['error']}"

        assistant_messages = [
            m for m in data.get("response", [])
            if m.get("role") == "assistant"
        ]

        return assistant_messages[-1]["content"] if assistant_messages else "No response."

    except requests.exceptions.ConnectionError:
        return "⚠️ Backend not reachable."
    except requests.exceptions.Timeout:
        return "⚠️ Request timed out."
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"


# UI HEADER
st.title("🤖 ChatPilot")
st.caption(f"Session: `{st.session_state.session_id}`")
st.divider()


# RENDER CHAT
def render_messages():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


render_messages()


# CHAT INPUT
prompt = st.chat_input("Type your message…")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_assistant_reply(
                prompt,
                st.session_state.session_id
            )
            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )


# SIDEBAR
with st.sidebar:
    st.header("⚙️ Controls")

    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

    st.divider()
    st.markdown("**Backend:** `localhost:8000`")
    st.markdown("**Model:** LangChain Agent")