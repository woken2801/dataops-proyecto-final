import pandas as pd
import os

print("Iniciando proceso...")

df = pd.read_csv("ComisionEmpleados_V1_202605.csv")

print(df.head())

os.makedirs("/output", exist_ok=True)

ruta = "/output/comisiones.xlsx"

df.to_excel(ruta, index=False)

print("Excel generado correctamente")
print("Archivo:", ruta)