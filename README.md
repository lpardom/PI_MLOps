# **Proyecto Individual 01**

Este proyecto tiene como objetivo desarrollar un sistema de recomendación de videojuegos para la empresa Steam, que se consume a través de una API. Además, se han creado funciones específicas para extraer datos relevantes de los conjuntos de datos proporcionados.

### Descripción del Proyecto
El proyecto se divide en varias etapas:

### 1. ETL (Extracción, Transformación y Carga)
Los datos se extrajeron de tres conjuntos de datos en formato JSON comprimidos y se limpiaron eliminando filas nulas, columnas irrelevantes y valores duplicados. Se realizaron transformaciones como normalizar fechas y realizar análisis de sentimientos para las reseñas de usuarios. Los datos limpios se guardaron en un archivo CSV para su uso posterior.

### 2. EDA (Análisis Exploratorio de Datos)
Se realizó un análisis exploratorio de datos utilizando las bibliotecas Seaborn, Matplotlib y Plotly para obtener información estadística sobre los conjuntos de datos y comprender mejor su estructura.

### 3. Funciones
Se desarrollaron cinco funciones específicas solicitadas por la empresa para extraer datos relevantes de los conjuntos de datos:

**PlayTimeGenre:** Devuelve el año con más horas jugadas para un género específico.

**UserForGenre:** Devuelve el usuario que acumula más horas jugadas para un género dado y una lista de la acumulación de horas jugadas por año.

### 5. Despliegue
Se creó una API utilizando FastAPI que expone las funciones desarrolladas. Se realizó un despliegue en la plataforma de Render.

### Requisitos
Los requisitos para ejecutar la API se encuentran en el archivo [requirements.txt](requirements.txt).
