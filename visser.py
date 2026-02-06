import streamlit as st
from chatbot_functies import chatbot_response

st.title("🐟 De Vermoeide Visser Bot")
st.caption("Praat met een grofgebekte, vermoeide zeeman. (Geen haat/geen expliciet.)")

if "history" not in st.session_state:
    st.session_state.history = []

user_msg = st.chat_input("Zeg eens wat, maat...")

if user_msg:
    st.session_state.history.append(("user", user_msg))

    systeemstijl = """
Je bent een vermoeide, grofgebekte visser die zijn hele leven op zee heeft gevist.
Je praat Nederlands met een stevig zeemansaccent en zee-woorden (boeg, bakboord, stuurboord, kombuis, dek).
Je bent kortaf, droog, een beetje cynisch. Gebruik milde scheldwoorden zoals "verdomme", "klootzak" spaarzaam.
GEEN haatdragende taal, GEEN discriminatie, GEEN expliciet seksuele inhoud.
"""

    # Maak er één prompt van (simpel, werkt met jouw huidige chatbot_response)
    prompt = systeemstijl + "\n\nGesprek:\n"
    for role, msg in st.session_state.history[-10:]:
        prompt += f"{role}: {msg}\n"
    prompt += "assistant:"

    with st.spinner("Even hijsen aan 't net..."):
        reply = chatbot_response(prompt)

    st.session_state.history.append(("assistant", reply))

# Toon gesprek
for role, msg in st.session_state.history:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.write(msg)
