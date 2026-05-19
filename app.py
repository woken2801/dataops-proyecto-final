import pandas as pd
import os

# Leer CSV
df = pd.read_csv('ComisionEmpleados_V1_202605.csv')

# Crear carpeta output
os.makedirs('output', exist_ok=True)

# Ruta del Excel
ruta = 'output/comisiones.xlsx'

# Generar Excel
df.to_excel(ruta, index=False)

print("Excel generado correctamente")
print("Archivo:", ruta)