import streamlit as st
from chatbot_functies import chatbot_response

st.set_page_config(page_title="De Vermoeide Visser Bot", page_icon="🐟")

st.title("🐟 De Vermoeide Visser Bot")
st.caption("Praat met een vermoeide, grofgebekte visser. Geen haat, geen expliciet.")

# Gesprekshistorie
if "history" not in st.session_state:
    st.session_state.history = []

# Input
user_msg = st.chat_input("Zeg eens wat, maat...")

if user_msg:
    st.session_state.history.append(("user", user_msg))

    systeemstijl = """
Je bent een vermoeide, grofgebekte visser die zijn hele leven op zee heeft gevist.
Je praat Nederlands met een stevig zeemansaccent en gebruikt zee-termen
zoals boeg, bakboord, stuurboord, dek en kombuis.

Je bent kortaf, cynisch en droog.
Milde scheldwoorden zijn toegestaan (zoals: verdomme, rotzooi, kloteweer),
maar GEEN haatdragende taal, GEEN discriminatie en GEEN expliciet seksuele inhoud.
"""

    prompt = systeemstijl + "\n\nGesprek:\n"
    for role, msg in st.session_state.history[-10:]:
        prompt += f"{role}: {msg}\n"
    prompt += "assistant:"

    with st.spinner("Even het net binnenhalen..."):
        antwoord = chatbot_response(prompt)

    st.session_state.history.append(("assistant", antwoord))

# Toon chat
for role, msg in st.session_state.history:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.write(msg)
