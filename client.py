
import requests
import streamlit as st

# a title to the application 
st.title("FastAPI ChatBot")


# Initialize the chat and keep track of the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat messages from the chat history on app rerun.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Wait until the user has submitted a prompt via the chat input field.
if prompt := st.chat_input("Write your prompt in this input field for text", key="text_input"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.text(prompt)

    response = requests.get(
        f"http://localhost:8000/generate/text", params={"prompt": prompt}
    )
    response.raise_for_status()

    with st.chat_message("assistant"):
        st.markdown(response.text)


