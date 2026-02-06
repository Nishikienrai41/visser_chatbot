import streamlit as st
from chatbot_functies import chatbot_response

st.set_page_config(page_title="De Vermoeide Visser Bot", page_icon="🐟")

# Kleine styling (kort en simpel)
st.markdown("""
<style>
.stApp { background: #06111f; }
.chatbox {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 18px;
}
.small { opacity: 0.85; }
</style>
""", unsafe_allow_html=True)

st.title("🐟 De Vermoeide Visser Bot")
st.markdown('<div class="small">Praat met een vermoeide, grofgebekte visser. Geen haat, geen expliciet.</div>', unsafe_allow_html=True)

# Gesprekshistorie
if "history" not in st.session_state:
    st.session_state.history = []

# Kleine extra: knop om chat te wissen
col1, col2 = st.columns([1, 1])
with col2:
    if st.button("🧹 Wis chat"):
        st.session_state.history = []
        st.rerun()

st.markdown('<div class="chatbox">', unsafe_allow_html=True)

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

st.markdown("</div>", unsafe_allow_html=True)
