from bumblebee import resquest, build_bumblebee
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# bumblebee = build_bumblebee()


st.set_page_config(
    page_title='Bumblebee | Chat',
    page_icon='🐝',
    layout='centered'
)
st.title("BUMBLEBEE CHAT 🐝")

if "message" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type heere"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # for response in resquest(bumblebee, prompt):
        #     full_response += response['result']
        #     message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(prompt + 'un instant')
    st.session_state.messages.append({"role": "assistant", "content": prompt + 'un instant'})