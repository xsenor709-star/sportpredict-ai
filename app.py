import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SportPredict AI",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ SportPredict AI")
st.subheader("Analizador Deportivo")

archivo = st.file_uploader(
    "Subí un archivo (.txt, .csv o .xlsx)",
    type=["txt", "csv", "xlsx"]
)

if archivo is not None:

    st.success("✅ Archivo cargado correctamente")

    if archivo.name.endswith(".txt"):
        contenido = archivo.read().decode("utf-8")

        lineas = contenido.splitlines()

        st.header("📊 Resumen del archivo")

        st.write(f"Total de líneas: {len(lineas)}")

        partidos = sum(1 for l in lineas if l.strip().startswith("*"))

        goles = sum(1 for l in lineas if "Min" in l or "1T" in l or "2T" in l)

        st.metric("Partidos encontrados", partidos)
        st.metric("Eventos de gol encontrados", goles)

        with st.expander("Ver contenido"):
            st.text(contenido[:5000])

    else:
        st.info("Por ahora solo analizaremos archivos TXT.")
