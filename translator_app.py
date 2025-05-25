import streamlit as st
from googletrans import Translator, LANGUAGES

st.set_page_config(page_title="AI Translator", layout="centered")
st.title("🌐 AI-Based Translator Website")

translator = Translator()

# Select language options
langs = list(LANGUAGES.values())
src_lang = st.selectbox("Translate from:", langs, index=langs.index("english"))
dest_lang = st.selectbox("Translate to:", langs, index=langs.index("french"))

# User input
text = st.text_area("Enter text to translate:")

# Translate button
if st.button("Translate"):
    try:
        # Get language codes
        src_code = list(LANGUAGES.keys())[langs.index(src_lang)]
        dest_code = list(LANGUAGES.keys())[langs.index(dest_lang)]

        translated = translator.translate(text, src=src_code, dest=dest_code)
        st.success(f"🔁 Translated Text: {translated.text}")
    except Exception as e:
        st.error(f"Translation failed: {e}")
