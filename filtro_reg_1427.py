from datos_pqr import cert_1427, reg_1427
import pandas as pd


datos = pd.DataFrame(reg_1427)

# Convertir la columna 'FECHA_LIMITE' al formato de fecha
datos['FECHA_LIMITE'] = pd.to_datetime(datos['FECHA_LIMITE'], errors='coerce')
datos['FECHA_DE_REMISION'] = pd.to_datetime(datos['FECHA_DE_REMISION'], errors='coerce')
datos['FECHA_INICIO'] = pd.to_datetime(datos['FECHA_INICIO'], errors='coerce')
datos['FECHA_FINAL'] = pd.to_datetime(datos['FECHA_FINAL'], errors='coerce')
datos['FECHA_DE_ENVIO_A_DPE'] = pd.to_datetime(datos['FECHA_DE_ENVIO_A_DPE'], errors='coerce')
datos['FECHA_DE_RESPUESTA_DPE'] = pd.to_datetime(datos['FECHA_DE_RESPUESTA_DPE'], errors='coerce')

# Formatear los valores de fechas en dataframe
datos['FECHA_LIMITE'] = datos['FECHA_LIMITE'].dt.strftime('%d/%m/%Y')
datos['FECHA_DE_REMISION'] = datos['FECHA_DE_REMISION'].dt.strftime('%d/%m/%Y')
datos['FECHA_INICIO'] = datos['FECHA_INICIO'].dt.strftime('%d/%m/%Y')
datos['FECHA_FINAL'] = datos['FECHA_FINAL'].dt.strftime('%d/%m/%Y')
datos['FECHA_DE_ENVIO_A_DPE'] = datos['FECHA_DE_ENVIO_A_DPE'].dt.strftime('%d/%m/%Y')
datos['FECHA_DE_RESPUESTA_DPE'] = datos['FECHA_DE_RESPUESTA_DPE'].dt.strftime('%d/%m/%Y')

# Formatear los valores a enteros
datos['DOCUMENTO'] = pd.to_numeric(datos['DOCUMENTO'], errors='coerce')
datos = datos.dropna(subset=['DOCUMENTO'])
datos['DOCUMENTO'] = datos['DOCUMENTO'].astype(int)

datos['NUMERO_PQR'] = pd.to_numeric(datos['NUMERO_PQR'], errors='coerce')
datos = datos.dropna(subset=['NUMERO_PQR'])
datos['NUMERO_PQR'] = datos['NUMERO_PQR'].astype(int)

datos['N_NCAPACIDAD_INICIAL'] = pd.to_numeric(datos['N_NCAPACIDAD_INICIAL'], errors='coerce')
datos = datos.dropna(subset=['N_NCAPACIDAD_INICIAL'])
datos['N_NCAPACIDAD_INICIAL'] = datos['N_NCAPACIDAD_INICIAL'].astype(int)

datos['N_INCAPACIDAD_FINAL'] = pd.to_numeric(datos['N_INCAPACIDAD_FINAL'], errors='coerce')
datos = datos.dropna(subset=['N_INCAPACIDAD_FINAL'])
datos['N_INCAPACIDAD_FINAL'] = datos['N_INCAPACIDAD_FINAL'].astype(int)
