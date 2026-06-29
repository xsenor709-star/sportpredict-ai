import streamlit as st

st.set_page_config(
    page_title="SportPredict AI",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ SportPredict AI")
st.subheader("Analizador Deportivo")

st.write("Bienvenido a la primera versión del proyecto.")

archivo = st.file_uploader(
    "Subí un archivo (.txt, .csv o .xlsx)",
    type=["txt", "csv", "xlsx"]
)

if archivo:
    st.success("✅ Archivo cargado correctamente")
    st.write("Nombre del archivo:", archivo.name)

st.divider()

st.header("📊 Estadísticas")
st.info("Próximamente aparecerán las estadísticas.")

st.header("🎯 Predicciones")
st.info("Disponible en la versión 0.2")
