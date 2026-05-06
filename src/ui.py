import streamlit as st
from components.layout import apply_layout
from screens.chat import render_chat_screen

def main():
    st.set_page_config(page_title="Chat App", layout="wide")
    apply_layout()
    render_chat_screen()

if __name__ == "__main__":
    main()
