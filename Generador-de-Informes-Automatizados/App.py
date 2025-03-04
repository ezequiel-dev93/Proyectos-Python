import streamlit as st

from crear_Plantilla import crear_plantilla
from generar_Informe import generar_docx
from generar_Excel import generar_excel

# Configuración principal de la app
st.title("Generador de Informes Automático")

# Selector de funcionalidad
opcion = st.selectbox("Seleccione una funcionalidad", ["Generar Informe", "Crear Plantilla Personalizada", "Crear Excel"])

# Ejecutar la funcionalidad seleccionada
if opcion == "Generar Informe":
    generar_docx()  # Llama a la función para generar el informe en Word

elif opcion == "Crear Plantilla Personalizada":
    crear_plantilla()  # Llama a la función para crear una plantilla personalizada

elif opcion == "Crear Excel":
    generar_excel()  # Llama a la función para generar el archivo Excel
