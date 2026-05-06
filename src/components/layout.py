import streamlit as st
import os

def apply_layout():
    # Carregar CSS global
    css_path = os.path.join(os.path.dirname(__file__), "..", "styles", "theme.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Montagem elementos globais (Sidebar, Header)
    st.sidebar.title("Navegação")
    st.sidebar.info("Estrutura modular profissional web.")
