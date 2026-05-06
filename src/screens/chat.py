import streamlit as st
import requests

API_URL = "http://backend:8000/api/v1/chat"

def render_chat_screen():
    st.header("Interface Chat")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Digite sua mensagem...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        try:
            res = requests.post(API_URL, json={"message": user_input})
            reply = res.json().get("reply", "Erro processamento.")
        except Exception:
            reply = "Falha conexão API v1."

        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
