import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno  
import janitor
import matplotlib.pyplot as plt
import missingno
import pyreadr
import seaborn as sns
import upsetplot

# Leer los datos
df = pd.read_excel('datos/JEFAB_2024.xlsx')

# Mostrar el tamaño del DataFrame
print(f"Tamaño del DataFrame: {df.shape}")

print(df.info())

# Análisis de datos faltantes
print("=== ANÁLISIS DE DATOS FALTANTES ===")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
print("Top 10 columnas con más datos faltantes:")
missing_info = pd.DataFrame({
'Columna': missing_data.index,
'Datos_Faltantes': missing_data.values,
'Porcentaje': missing_percent.values
}).sort_values('Datos_Faltantes', ascending=False)
print(missing_info.head(10))
# Análisis de duplicados
print(f"\n=== ANÁLISIS DE DUPLICADOS ===")
print(f"Registros duplicados: {df.duplicated().sum()}")
# Análisis de tipos de datos
print(f"\n=== TIPOS DE DATOS ===")
print(df.dtypes.value_counts())
# Identificar columnas problemáticas
print(f"\n=== COLUMNAS CON CARACTERES ESPECIALES ===")
problematic_columns = [col for col in df.columns if 'Ã' in col or 'â' in col]
print(f"Columnas con encoding problemático: {len(problematic_columns)}")
for col in problematic_columns[:5]:
    print(f" - {col}")
#nueva linea


# Matriz Datos Faltantes
from upsetplot import UpSet
from upsetplot import from_contents
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

missing_by_column = {col: df.index[df[col].isnull()] for col in df.columns if df[col].isnull().any()}
upset_data = from_contents(missing_by_column)

upset = UpSet(upset_data)
upset.plot()
plt.show()

# Imputación MICE
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

# Selecciona solo las columnas numéricas para imputación
numeric_cols = df.select_dtypes(include=[np.number]).columns
imputer = IterativeImputer(random_state=0)
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

print("Imputación MICE completada para columnas numéricas.")

faltantes_post = df[numeric_cols].isnull().sum()
print("\nDatos faltantes por columna después de la imputación MICE:")
print(faltantes_post)
# Si quieres ver el total de faltantes:
print(f"Total de datos faltantes después de imputación: {faltantes_post.sum()}")
# ...existing code...