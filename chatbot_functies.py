import os
import streamlit as st
import cohere

def _get_cohere_key() -> str:
    # Streamlit Cloud secrets (online)
    if "COHERE_API_KEY" in st.secrets:
        return st.secrets["COHERE_API_KEY"]

    # Lokale environment variable (optioneel)
    return os.getenv("COHERE_API_KEY", "")

def chatbot_response(prompt: str) -> str:
    api_key = _get_cohere_key()

    if not api_key:
        return "Geen COHERE_API_KEY gevonden. Voeg deze toe via Streamlit Secrets."

    co = cohere.Client(api_key)
    response = co.chat(message=prompt)

    return response.text
