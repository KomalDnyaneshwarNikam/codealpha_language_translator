import streamlit as st
from googletrans import Translator, LANGUAGES

st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="centered")

st.title("🌍 Language Translation Tool")
st.markdown("### CodeAlpha AI Internship - Task 1")

translator = Translator()

# Language selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "From Language",
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x].title(),
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "To Language",
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x].title(),
        index=21   # Hindi by default
    )

text = st.text_area("Enter text to translate:", height=180, placeholder="Type or paste your text here...")

if st.button("🔄 Translate", type="primary"):
    if text.strip():
        with st.spinner("Translating..."):
            try:
                result = translator.translate(text, src=source_lang, dest=target_lang)
                
                st.success("✅ Translation Successful!")
                st.subheader("Translated Text:")
                st.write(f"**{result.text}**")
                
                st.info(f"Detected Source Language: **{LANGUAGES.get(result.src, result.src).title()}**")
                
            except Exception as e:
                st.error(f"Translation failed. Try again. ({str(e)})")
    else:
        st.warning("Please enter some text!")

st.caption("Built for CodeAlpha AI Internship • Task 1")