# datos_exploracion.py (archivo principal conjunto)
import pandas as pd
import matplotlib.pyplot as plt
# Importar funciones de cada miembro
from demografia_basica import analizar_demografia
from analisis_familiar import analizar_familia
from calidad_datos import evaluar_calidad
def main():
# Cargar datos
    df = pd.read_excel('datos/JEFAB_2024.xlsx')
    print("=== REPORTE CONJUNTO EQUIPO X ===")
# Ejecutar análisis de cada miembro
    analizar_demografia(df)
    analizar_familia(df)
    evaluar_calidad(df)
    print("=== ANÁLISIS COMPLETADO ===")
