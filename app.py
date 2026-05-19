import pandas as pd
import os

df = pd.read_csv('ComisionEmpleados_V1_202605.csv')

os.makedirs('/app/output', exist_ok=True)

ruta = '/app/output/comisiones.xlsx'

df.to_excel(ruta, index=False)

print("Excel generado correctamente")
print("Archivo:", ruta)