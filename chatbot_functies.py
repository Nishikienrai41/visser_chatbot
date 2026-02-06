import os
import streamlit as st
import cohere

def _get_cohere_key() -> str:
    # 1) Streamlit Cloud secrets
    if "COHERE_API_KEY" in st.secrets:
        return st.secrets["COHERE_API_KEY"]
    # 2) Lokale env var (optioneel)
    return os.getenv("COHERE_API_KEY", "")

def chatbot_response(prompt: str) -> str:
    """Stuurt een prompt naar Cohere en geeft het antwoord terug."""
    api_key = _get_cohere_key()
    if not api_key:
        return "Geen COHERE_API_KEY gevonden. Voeg die toe via Streamlit secrets."
    co = cohere.Client(api_key)
    response = co.chat(message=prompt)
    return response.text
