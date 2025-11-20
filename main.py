import streamlit as st 

st.set_page_config(
    page_icon="assets/favicon.ico",
    page_title="TRADUCTOR | Streamlit"
)

pages = {
    "Servicios": [
        st.Page("traductor.py", title="Traductor", icon=":material/translate:"),
        st.Page("traductor_archivos.py", title="Traductor de Archivos", icon=":material/g_translate:"),
    ]
}

pg = st.navigation(
    pages=pages, 
    position="sidebar", 
    expanded=True
)
pg.run()

