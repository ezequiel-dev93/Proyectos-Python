import streamlit as st
from io import BytesIO
import pandas as pd

def generar_excel():
    st.title("Generador de Presupuesto/Importe en Excel")
    st.write("Crea y descarga un archivo Excel con tus importes o gastos.")

    # Selección de moneda
    moneda = st.selectbox("Seleccione el símbolo de la moneda", ["$", "€", "£", "¥", "₿", "₽", "₹"])

    # Entrada de datos
    columnas = st.text_input("Ingrese las columnas separadas por comas", "Fecha, Concepto, Importe")
    datos = st.text_area("Ingrese los datos separados por comas y por filas (una fila por línea)", "2024-11-02, Compras, 150")

    # Convertir a DataFrame
    try:
        columnas = [col.strip() for col in columnas.split(",")]
        filas = [fila.split(",") for fila in datos.split("\n")]

        # Crear el DataFrame y agregar el símbolo de moneda al campo de Importe
        df = pd.DataFrame(filas, columns=columnas)
        if "Importe" in df.columns:
            df["Importe"] = df["Importe"].apply(lambda x: f"{moneda}{x.strip()}")  # Aplicar símbolo

    except Exception as e:
        st.error("Error en el formato de datos. Verifique las entradas.")
        return

    # Guardar en BytesIO y descargar
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    buffer.seek(0)

    st.download_button(
        label="Descargar Archivo Excel",
        data=buffer,
        file_name="presupuesto.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    buffer.close()

# Ejecutar la función si este archivo se corre directamente
if __name__ == "__main__":
    generar_excel()
