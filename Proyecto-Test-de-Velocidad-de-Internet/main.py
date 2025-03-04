import streamlit as st
import speedtest

# Función principal
def main():
    st.header("Test de Velocidad de Internet")
    st.write("Haga clic en el botón para iniciar el test.")

    if st.button("Iniciar"):
        with st.spinner("Testeando la velocidad de su internet..."):
            test = speedtest.Speedtest()
            test.get_best_server()
            download_speed = test.download() / 1_000_000  # Convertimos a Mbps
            upload_speed = test.upload() / 1_000_000     # Convertimos a Mbps
            results = test.results.dict()

            max_speed = 100  # Límite de referencia para la barra de progreso

            # Muestramos la velocidad de descarga
            st.write(f"Velocidad de descarga: {download_speed:.2f} Mbps")
            st.progress(min(download_speed / max_speed, 1.0))

            # Muestramos la velocidad de subida
            st.write(f"Velocidad de subida: {upload_speed:.2f} Mbps")
            st.progress(min(upload_speed / max_speed, 1.0))

            # Muestramos el ping
            st.write(f"Ping: {results['ping']} ms")

# Ejecutamos la función principal
main()
