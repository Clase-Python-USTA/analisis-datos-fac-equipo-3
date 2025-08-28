# Hallazgos del análisis de calidad de datos

## 1. Visualización de datos faltantes

Se realizó una visualización tipo UpSet para identificar las combinaciones de columnas con datos faltantes.

## 2. Filtro de columnas solicitado por los compañeros A y B

Por solicitud de los compañeros A y B, se filtró el DataFrame para trabajar únicamente con las siguientes columnas relevantes para el análisis:

- SEXO
- GENERO
- EDAD2
- ESTRATO
- NIVEL_EDUCATIVO
- NUMERO_PERSONAS_APORTE_SOSTENIMIENTO2
- NUMERO_HABITAN_VIVIENDA2
- NUMERO_HIJOS
- HIJOS_EN_HOGAR
- EDAD_RANGO_PADRE
- EDAD_PADRE
- EDAD_RANGO_MADRE
- EDAD_MADRE
- EDAD_RANGO
- ESTADO_CIVIL
- HIJOS
- HABITA_VIVIENDA_FAMILIAR
- MADRE_VIVE_SI
- MADRE_VIVE_NO
- NUMERO_HIJOS_RANGO
- GRADO
- NIVEL EDUCATIVO

## 3. Imputación de datos faltantes

Se imputaron los valores faltantes en las columnas numéricas utilizando el método MICE.

## 4. Validación de resultados

No quedaron datos faltantes en las columnas numéricas seleccionadas.  
Se imprimieron las primeras filas del DataFrame imputado y filtrado para verificar la correcta aplicación del proceso.

## 5. Resumen adicional

- Columnas con más datos faltantes: ver tabla generada.
- Registros duplicados: no se encontraron.
- Problemas de encoding: no se detectaron.
