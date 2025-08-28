import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno  
import pyreadr
import seaborn as sns
import warnings
from upsetplot import UpSet, from_contents
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

warnings.simplefilter(action='ignore', category=FutureWarning)

# ======================================================
# 1. Cargar los datos
# ======================================================
df = pd.read_excel('datos/JEFAB_2024.xlsx')
print(f"Tamaño del DataFrame original: {df.shape}")
print(df.info())

# ======================================================
# 2. Análisis inicial de datos faltantes
# ======================================================
print("\n=== ANÁLISIS DE DATOS FALTANTES (DataFrame completo) ===")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
missing_info = pd.DataFrame({
    'Columna': missing_data.index,
    'Datos_Faltantes': missing_data.values,
    'Porcentaje': missing_percent.values
}).sort_values('Datos_Faltantes', ascending=False)
print(missing_info.head(10))

# Visualización con UpSet
missing_by_column = {col: df.index[df[col].isnull()] for col in df.columns if df[col].isnull().any()}
upset_data = from_contents(missing_by_column)
upset = UpSet(upset_data)
upset.plot()
plt.show()

# ======================================================
# 3. Filtrar columnas antes de imputación
# ======================================================
columnas_filtrar = [
    "SEXO", "GENERO", "EDAD2", "ESTRATO", "NIVEL_EDUCATIVO",
    "NUMERO_PERSONAS_APORTE_SOSTENIMIENTO2", "NUMERO_HABITAN_VIVIENDA2",
    "NUMERO_HIJOS", "HIJOS_EN_HOGAR", "EDAD_RANGO_PADRE", "EDAD_PADRE",
    "EDAD_RANGO_MADRE", "EDAD_MADRE", "EDAD_RANGO", "ESTADO_CIVIL",
    "HIJOS", "HABITA_VIVIENDA_FAMILIAR", "MADRE_VIVE_SI", "MADRE_VIVE_NO",
    "NUMERO_HIJOS_RANGO", "GRADO", "NIVEL EDUCATIVO"
]

columnas_existentes = [col for col in columnas_filtrar if col in df.columns]
df_filtrado = df[columnas_existentes]


# ======================================================
# 4. Imputación MICE en columnas numéricas del DataFrame filtrado
# ======================================================
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

# Columnas numéricas
numeric_cols = df_filtrado.select_dtypes(include=[np.number]).columns
print(f"\nColumnas numéricas a imputar: {list(numeric_cols)}")

# Imputador con restricción de valores mínimos
imputer = IterativeImputer(random_state=0, min_value=0)
df_filtrado[numeric_cols] = imputer.fit_transform(df_filtrado[numeric_cols])

print("\nImputación MICE completada en DataFrame filtrado (sin negativos).")

# ======================================================
# 4.1 Redondear columnas de conteos
# ======================================================
conteos_cols = ["NUMERO_HIJOS", "HIJOS_EN_HOGAR", "NUMERO_PERSONAS_APORTE_SOSTENIMIENTO2",
                "NUMERO_HABITAN_VIVIENDA2", "NUMERO_HIJOS_RANGO"]

# Redondear y convertir a enteros SOLO si existen en el DataFrame
for col in conteos_cols:
    if col in df_filtrado.columns:
        df_filtrado[col] = df_filtrado[col].round().astype(int)

print("\nColumnas de conteos redondeadas a enteros.")

# ======================================================
# 5. Validación de resultados
# ======================================================
faltantes_post = df_filtrado[numeric_cols].isnull().sum()
print("\nDatos faltantes por columna después de imputación:")
print(faltantes_post)
print(f"Total de datos faltantes después de imputación: {faltantes_post.sum()}")

print("\nPrimeras filas del DataFrame imputado y filtrado:")
print(df_filtrado.head())

# 1. Columnas con más datos faltantes
print("\n=== Columnas con más datos faltantes ===")
print(missing_info.head(10))

# 2. Registros duplicados
print("\n=== ANÁLISIS DE DUPLICADOS ===")
print(f"Registros duplicados: {df.duplicated().sum()}")

# 3. Problemas de encoding
print("\n=== Problemas de encoding en nombres de columnas ===")
problematic_columns = [col for col in df.columns if not all(ord(c) < 128 for c in col)]
print(f"Columnas con encoding problemático: {len(problematic_columns)}")
for col in problematic_columns:
    print(f" - {col}")