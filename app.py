import pandas as pd
import psycopg2
import os

conexion = psycopg2.connect(
    host="mgg.vps.webdock.cloud",
    database="dmc",
    user="usr_ro_dmc_rrhh_estudiantes",
    password="fZp!jHt0j6%89^B4I*L*29bz4b^",
    port="5432"
)

query = '''
SELECT empleado_id,
       nom_empleado,
       ape_empleado,
       mnt_salario,
       mnt_tope_comision
FROM rrhh.Empleado
'''

df = pd.read_sql(query, conexion)

df["comision_calculada"] = df["mnt_salario"] * 0.10

os.makedirs("output", exist_ok=True)

ruta = "output/comisiones.xlsx"

df.to_excel(ruta, index=False)

print("Excel generado correctamente")
print(df.head())
