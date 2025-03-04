# Proyecto - Generador de Informes Personalizados en Word
Este proyecto permite la creación de informes personalizados en formato Word, utilizando datos cargados desde archivos Excel o CSV y la visualización opcional de gráficos generados con matplotlib. La aplicación está construida con Python y Streamlit, lo que facilita su ejecución como una aplicación web interactiva.


## Características
* Cargar plantillas de Word: Se puede cargar un archivo .docx como plantilla, con marcadores para ser reemplazados por valores personalizados.

* Integración con datos externos: Los datos se importan desde archivos .xlsx o .csv y se muestran en la aplicación para su visualización y selección.

* Generación de gráficos: Permite crear gráficos personalizados que se insertan automáticamente en el informe.

* Descarga de informes: Los informes generados se pueden descargar en formato Word, incluyendo los datos personalizados y gráficos.

## Tecnologías Utilizadas
* Python: Lenguaje principal del proyecto.
* Streamlit: Interfaz de usuario interactiva y sencilla para aplicaciones web.
* Pandas: Manejo y procesamiento de datos.
* python-docx: Manipulación y creación de documentos Word.
* matplotlib: Generación de gráficos personalizados.
* io: Manipulación de flujos de datos para guardar y cargar gráficos en la plantilla.

## Requisitos de instalación
* Clona este repositorio
* Carga la plantilla de Word y el archivo de datos (Excel o CSV).
* Configura las opciones para seleccionar filas de datos y generar gráficos.
* Descarga el informe en formato .docx.


## Uso
* Inicia la aplicación: streamlit run app.py
* Carga la plantilla de Word y el archivo de datos (Excel o CSV).
* Configura las opciones para seleccionar filas de datos y generar gráficos.
* Descarga el informe en formato .docx.

## Ejemplo de Plantilla de Word
Para utilizar esta aplicación, tu plantilla de Word debe contener marcadores en formato {{campo}}, donde campo es el nombre de la columna del archivo de datos.
**Ejemplo**

Informe de Ventas para {{nombre_cliente}}

Fecha: {{fecha}}

Total de Ventas: {{total_ventas}}

[Aqui se insertará el gráfico]

## Contribuciones
Las contribuciones son bienvenidas. Si tienes sugerencias o encuentras algún error, no dudes en abrir un issue o enviar un pull request.

## Creditos
Este proyecto fue desarrollado en Visual Studio Code, utilizando Python y la biblioteca Streamlit.
Agradecimientos especiales a las siguientes herramientas y bibliotecas que facilitaron el desarrollo de esta aplicación:

* Python: para la programación principal y manipulación de datos.
* Streamlit: para la creación de una interfaz interactiva y amigable.
* Docx: para generar documentos de Word personalizados.
* Pandas y Matplotlib: para el manejo y visualización de datos.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.