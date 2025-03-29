import streamlit as st
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from bumblebee import resquest, build_bumblebee

from langchain_ollama import ChatOllama

def ui():
    st.set_page_config(
        page_title='Bumblebee | chat',
        page_icon='🐝'
    )

    bumblebee = build_bumblebee()

    if "messages" != st.session_state:
        st.session_state.messages = [
            SystemMessage(content="Your are a helpful assistant.")
        ]

    prompt = st.chat_input('Type here')

    if prompt:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("human", avatar="🧑"):
            st.write(prompt)
        
        with st.spinner("Thinking", show_time=True):
            response = resquest(bumblebee, prompt)

        with st.chat_message("ai", avatar="🐝"):
            st.markdown(response['answer'])
        st.session_state.messages.append(AIMessage("Salut, je suis un assistant IA"))

           
        

if __name__ == "__main__":
    ui()