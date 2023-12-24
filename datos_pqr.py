import os
import pandas as pd
import numpy as np
import openpyxl as op
import warnings 
warnings.simplefilter('ignore')

#conectores 
pqr_datos = os.path.join(r"C:\Users\dapache\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS", "consolidado.txt")
reg_datos = os.path.join(r"C:\Users\dapache\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS", "certificados_1427_PQRS.xlsx")

#Lectura de datos
try:
    cert_1427 = pd.read_csv(pqr_datos, sep=';', encoding='ISO-8859-1', index_col=None, header=0)
except FileNotFoundError:
    raise FileNotFoundError(f"No se encontró el archivo CSV en {pqr_datos}.")

try:
    reg_1427 = pd.read_excel(reg_datos, sheet_name='CERTIFICADO_PQRS', header=0)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo Excel en {reg_datos}.")
    reg_1427 = pd.DataFrame()

# Convertir la columna 'FECHA_LIMITE' al formato de fecha
reg_1427['FECHA_LIMITE'] = pd.to_datetime(reg_1427['FECHA_LIMITE'], errors='coerce')
reg_1427['FECHA_DE_REMISION'] = pd.to_datetime(reg_1427['FECHA_DE_REMISION'], errors='coerce')
reg_1427['FECHA_INICIO'] = pd.to_datetime(reg_1427['FECHA_INICIO'], errors='coerce')
reg_1427['FECHA_FINAL'] = pd.to_datetime(reg_1427['FECHA_FINAL'], errors='coerce')
reg_1427['FECHA_DE_ENVIO_A_DPE'] = pd.to_datetime(reg_1427['FECHA_DE_ENVIO_A_DPE'], errors='coerce')
reg_1427['FECHA_DE_RESPUESTA_DPE'] = pd.to_datetime(reg_1427['FECHA_DE_RESPUESTA_DPE'], errors='coerce')

# Formatear los valores de fechas en dataframe
reg_1427['FECHA_LIMITE'] = reg_1427['FECHA_LIMITE'].dt.strftime('%d/%m/%Y')
reg_1427['FECHA_DE_REMISION'] = reg_1427['FECHA_DE_REMISION'].dt.strftime('%d/%m/%Y')
reg_1427['FECHA_INICIO'] = reg_1427['FECHA_INICIO'].dt.strftime('%d/%m/%Y')
reg_1427['FECHA_FINAL'] = reg_1427['FECHA_FINAL'].dt.strftime('%d/%m/%Y')
reg_1427['FECHA_DE_ENVIO_A_DPE'] = reg_1427['FECHA_DE_ENVIO_A_DPE'].dt.strftime('%d/%m/%Y')
reg_1427['FECHA_DE_RESPUESTA_DPE'] = reg_1427['FECHA_DE_RESPUESTA_DPE'].dt.strftime('%d/%m/%Y')

# Formatear los valores nulos y floats to int
reg_1427['DOCUMENTO'] = pd.to_numeric(reg_1427['DOCUMENTO'], errors='coerce')
reg_1427 = reg_1427.dropna(subset=['DOCUMENTO'])
reg_1427['DOCUMENTO'] = reg_1427['DOCUMENTO'].astype(int)

reg_1427['NUMERO_PQR'] = pd.to_numeric(reg_1427['NUMERO_PQR'], errors='coerce')
reg_1427 = reg_1427.dropna(subset=['NUMERO_PQR'])
reg_1427['NUMERO_PQR'] = reg_1427['NUMERO_PQR'].astype(int)

reg_1427['N_NCAPACIDAD_INICIAL'] = pd.to_numeric(reg_1427['N_NCAPACIDAD_INICIAL'], errors='coerce')
reg_1427 = reg_1427.dropna(subset=['N_NCAPACIDAD_INICIAL'])
reg_1427['N_NCAPACIDAD_INICIAL'] = reg_1427['N_NCAPACIDAD_INICIAL'].astype(int)

reg_1427['N_INCAPACIDAD_FINAL'] = pd.to_numeric(reg_1427['N_INCAPACIDAD_FINAL'], errors='coerce')
reg_1427 = reg_1427.dropna(subset=['N_INCAPACIDAD_FINAL'])
reg_1427['N_INCAPACIDAD_FINAL'] = reg_1427['N_INCAPACIDAD_FINAL'].astype(int)

# Crear DataFrame a partir de cert_1427
datos_cert_1427 = pd.DataFrame(cert_1427)
# Poner nombre a la columna de datos
datos_cert_1427.columns = ['Datos']
# Dividir la columna 'Datos' en columnas separadas
datos_cert_1427[['TD', 'Documento', 'Nombre1', 'Nombre2', 'Nombre3', 'Apellido1', 'Apellido2', 'Apellido3']] = datos_cert_1427['Datos'].str.split(' ', expand=True, n=7)