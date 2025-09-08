# analisis-datos-fac-equipo-3

## Descripción General del Proyecto

#### Fredy Chavarro - Hayder Rodriguez - Ricardo Vargas

Este proyecto tiene como objetivo realizar un análisis exploratorio de un conjunto de datos (`JEFAB_2024.xlsx`) para comprender las características de la población estudiada. Estan son sus etapas:

1.  **Carga de Datos:** Se ha cargado el conjunto de datos desde un archivo Excel a un DataFrame de pandas.
2.  **Análisis Inicial de Datos Faltantes:** Se ha realizado una inspección inicial para identificar la cantidad y el porcentaje de datos faltantes en cada columna, utilizando tablas y visualizaciones como el gráfico UpSet para entender las combinaciones de valores faltantes.
3.  **Filtrado de Columnas:** Se ha creado un subconjunto del DataFrame original seleccionando columnas relevantes para el análisis, especialmente aquellas relacionadas con características demográficas y familiares.
4.  **Imputación de Datos Faltantes:** Se ha aplicado la técnica de imputación MICE (Multiple Imputation by Chained Equations) en las columnas numéricas del DataFrame filtrado para rellenar los valores faltantes, asegurando que los valores imputados no sean negativos y redondeando las columnas de conteo a enteros.
5.  **Validación de la Imputación:** Se ha verificado que no queden datos faltantes en las columnas numéricas después de la imputación y se han inspeccionado las primeras filas del DataFrame imputado y filtrado.
6.  **Análisis Familiar:** Se ha realizado un análisis de las variables relacionadas con la estructura familiar, incluyendo la distribución del estado civil, la presencia de hijos, la convivencia familiar y la relación entre la edad y el estado civil. Se han generado gráficos (barras, cajas, histogramas) y tablas para visualizar estos hallazgos.
7.  **Análisis Demográfico:** Se llevó a cabo un análisis de las principales variables demográficas, considerando la distribución por sexo, los rangos de edad, el nivel educativo y el grado militar del personal de la FAC. Para facilitar la interpretación de los resultados se emplearon diferentes representaciones gráficas (barras, histogramas y gráficos de torta), así como tablas que resumen los hallazgos más relevantes.

En resumen, el proyecto se encuentra en una fase de exploración y limpieza de datos, con un enfoque inicial en la comprensión de las dinámicas familiares dentro del conjunto de datos, abordando la presencia de datos faltantes y preparando las variables para análisis posteriores.
