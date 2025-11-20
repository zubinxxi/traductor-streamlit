import streamlit as st
import pyperclip
import pandas as pd
from deep_translator import GoogleTranslator #Limite de 5000 caracteres como máximo a traducir
from docx import Document
from pypdf import PdfReader
from streamlit_extras.no_default_selectbox import selectbox as no_df_selectbox

st.title("Traductor de Archivos")

def copy_text(text):
    pyperclip.copy(text)

languages = {
    'Español':'es',
    'Inglés':'en',
    'Francés':'fr',
    'Alemán':'de',
    'Italiano':'it'
}

target_lang = no_df_selectbox(
    "Idioma de destino:", 
    options=list(languages.keys()), 
    no_selection_label="Seleccionar"
)

file = st.file_uploader(
    "Sube un archivo (.txt, .docx, .pdf, .csv):", 
    type=["txt","docx","pdf","csv"],
)

if file:
    text_content = ""
    try:
        if file.name.endswith(".txt"):
            text_content = file.read().decode("utf-8")
        elif file.name.endswith(".docx"):
            doc = Document(file)
            text_content = "\n".join([p.text for p in doc.paragraphs])
        elif file.name.endswith(".pdf"):
            pdf_reader = PdfReader(file)
            text_content = "\n".join([page.extract_text() for page in pdf_reader.pages])
        elif file.name.endswith(".csv"):
            df = pd.read_csv(file)
            text_content = df.to_csv(index=False)

        st.text_area("Contenido del archivo:", text_content, height=300)

        if st.button("Traducir", icon=":material/translate:"):
            if target_lang:
                translated_text = GoogleTranslator(
                    source='auto',
                    target=languages[target_lang]
                ).translate(text_content)
                st.success("Traducción completa.")
                st.text_area("Texto traducido:", translated_text, height=300)        
                st.button("Copiar", icon=":material/file_copy:", type="primary", on_click=copy_text(translated_text))
            else:
                st.error("Seleccione el idioma destino.")

    except Exception as e:
        print(e)
        st.error(f"Error al procesar el archivo.")