import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno  
import pyreadr
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




#ANÁLISIS DEMOGRAFICO

# Leer los datos
df = pd.read_excel('/content/JEFAB_2024.xlsx')


# Explorar estructura básica
print("=== INFORMACIÓN GENERAL ===")
print(f"Total de registros: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")


# Análisis de edad
print("\n=== ANÁLISIS DE EDAD ===")
print(f"Rango de edades: {df['EDAD2'].min()}-{df['EDAD2'].max()} años")
print(f"Edad promedio: {df['EDAD2'].mean():.1f} años")
print(f"Edad mínima: {df['EDAD2'].min()} años")
print(f"Edad máxima: {df['EDAD2'].max()} años")


# Gráfico de edades
plt.figure(figsize=(10, 6))
plt.hist(df['EDAD2'], bins=20, edgecolor='black')
plt.title('Distribución de Edades del Personal FAC')
plt.xlabel('Edad')
plt.ylabel('Cantidad de Personal')
plt.show()

# 1. ¿Cuál es el rango de edad más común?

moda = df['EDAD2'].mode()[0] # Calcular la moda (el valor que más se repite) en la columna 'EDAD2'
print("La edad más común es:", moda,"años") # Imprimir la moda con un mensaje

# 2. ¿Hay diferencias en la distribución por Sexo?

# distribucion por Sexo
sexo_counts = df['SEXO'].value_counts()  # Contar la cantidad de cada valor en la columna 'SEXO'

plt.figure(figsize=(7,7)) # Crear la figura del gráfico y definir el tamaño
plt.pie(sexo_counts, #  los valores (ej: cuántos hombres y mujeres)
        labels=sexo_counts.index, # las etiquetas (ej: "Hombre", "Mujer")
        autopct='%1.1f%%'), # muestra el porcentaje con 1 decimal
plt.title("Distribución por Sexo") ## Título del gráfico
plt.show() # # Mostrar en pantalla

# Cuenta cuantos hombres y mujeres hay 
conteo = df['SEXO'].value_counts(normalize=False) # Contar la cantidad de cada categoría en la columna 'SEXO' # normalize=False → cuenta el número de registros
porcentaje = df['SEXO'].value_counts(normalize=True)*100  # Calcular el porcentaje de cada categoría, # # normalize=True → calcula proporciones ,#*100 → lo convierte en porcentaje

# Mostrar resultados en consola
print("\n=== ANÁLISIS DE GÉNERO ===") # Mostrar resultados en consola
print(pd.DataFrame({"Cantidad": conteo, "Porcentaje %": porcentaje.round(3).astype(str) + " %"})) # Crear una tabla que muestre las cantidades y porcentajes, # - round(3) redondea a 3 decimales,## - astype(str) + " %"  convierte en texto y le agrega el símbolo %

# Nivel educativo por sexo ---
plt.figure(figsize=(10,6)) # Crear la figura del gráfico y definir el tamaño (ancho=10, alto=6)
sns.countplot(data=df, x="NIVEL_EDUCATIVO", hue="SEXO") # Gráfico de barras con Seaborn (countplot),#data=df → usa los datos del DataFrame, hue="SEXO" → divide cada barra por sexo
plt.title("Nivel Educativo según el sexo")
plt.show()

# Nivel de Estrato por sexo ---
plt.figure(figsize=(10,6)) # Crear la figura del gráfico y definir el tamaño (ancho=10, alto=6)
sns.countplot(data=df, x="ESTRATO", hue="SEXO") # Gráfico de barras con Seaborn (countplot),#data=df → usa los datos del DataFrame, hue="SEXO" → divide cada barra por sexo
plt.title("Estrato según el sexo")
plt.show()

# hijos por género ---
plt.figure(figsize=(10,6)) # Crear la figura del gráfico y definir el tamaño (ancho=10, alto=6)
sns.countplot(data=df, x="HIJOS", hue="SEXO") # Gráfico de barras con Seaborn (countplot),#data=df → usa los datos del DataFrame, hue="SEXO" → divide cada barra por sexo
plt.title("hijos por sexo")
plt.show()

# 3. ¿Cuál es el grado militar más frecuente?

frecuencias = df['GRADO'].value_counts() # Calcular la frecuencia de cada grado militar en la columna 'GRADO'
print(frecuencias.head(18)) # Mostrar los 18 primeros grados con mayor frecuencia
print("\nEl grado militar más frecuente es:", frecuencias.idxmax(), "con", frecuencias.max(), "personas")## Imprimir el grado más común con la cantidad de personas que lo tienen,## - idxmax() → devuelve el nombre del grado con mayor frecuencia, # - max() → devuelve cuántas personas hay en ese grado


# Gráfico de barras de grados militares (versión sencilla)
frecuencias.plot.bar() # Hacer un gráfico de barras con las frecuencias de los grados militare
plt.title("Distribución de Grados Militares") # Poner título al gráfico
plt.show()#mostrar


# Gráfica de Distribución de Grados Militares por Sexo
plt.figure(figsize=(12,6)) # Crear una figura y definir el tamaño del gráfico (ancho=12, alto=6)
sns.countplot(data=df, x="GRADO", hue="SEXO",order=df['GRADO'].value_counts().index) # - order=df['GRADO'].value_counts().index → ordena los grados según su frecuencia (más comunes primero)
plt.xticks(rotation=45) # Rotar las etiquetas del eje X 45 grados para que se lean mejor
plt.title("Distribución de Grados Militares por Sexo") # Poner título al gráfico
plt.show()

#añado eñ código de colab
# https://colab.research.google.com/drive/1R2SJd3UIARMzy6lCdaNYP596ye9KiqAz?usp=sharing
