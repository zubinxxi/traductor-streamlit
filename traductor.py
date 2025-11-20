import streamlit as st
from deep_translator import GoogleTranslator #Limite de 5000 caracteres como máximo a traducir
import pyperclip
from streamlit_extras.no_default_selectbox import selectbox as no_df_selectbox

st.title("Traductor")
languages = {
    'Español':'es',
    'Inglés':'en',
    'Francés':'fr',
    'Alemán':'de',
    'Italiano':'it'
}

def copy_text(text):
    pyperclip.copy(text)

text_to_translate = st.text_area("Escribe el texto a traducir")

target_lang = no_df_selectbox(
    "Idioma de destino", 
    options=list(languages.keys()), 
    no_selection_label="Seleccionar"
)

if st.button("Traducir"):
    if text_to_translate:
        try:
            translated_text = GoogleTranslator(
                source='auto',
                target=languages[target_lang]
            ).translate(text_to_translate)

            st.success(f"Traducción: {translated_text}")
            st.button("Copiar", icon=":material/file_copy:", type="primary", on_click=copy_text(translated_text))

        except Exception as e:
            print(e)
            st.error(f"Error al traducir: {e}")
    else:
        st.warning("Escribe un texto")
