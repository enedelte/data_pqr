from datos_pqr import cert_1427, reg_1427
import pandas as pd


datos_reg_1427 = pd.DataFrame(reg_1427)

# Convertir la columna 'FECHA_LIMITE' al formato de fecha
datos_reg_1427['FECHA_LIMITE'] = pd.to_datetime(datos_reg_1427['FECHA_LIMITE'], errors='coerce')
datos_reg_1427['FECHA_DE_REMISION'] = pd.to_datetime(datos_reg_1427['FECHA_DE_REMISION'], errors='coerce')
datos_reg_1427['FECHA_INICIO'] = pd.to_datetime(datos_reg_1427['FECHA_INICIO'], errors='coerce')
datos_reg_1427['FECHA_FINAL'] = pd.to_datetime(datos_reg_1427['FECHA_FINAL'], errors='coerce')
datos_reg_1427['FECHA_DE_ENVIO_A_DPE'] = pd.to_datetime(datos_reg_1427['FECHA_DE_ENVIO_A_DPE'], errors='coerce')
datos_reg_1427['FECHA_DE_RESPUESTA_DPE'] = pd.to_datetime(datos_reg_1427['FECHA_DE_RESPUESTA_DPE'], errors='coerce')

# Formatear los valores de fechas en dataframe
datos_reg_1427['FECHA_LIMITE'] = datos_reg_1427['FECHA_LIMITE'].dt.strftime('%d/%m/%Y')
datos_reg_1427['FECHA_DE_REMISION'] = datos_reg_1427['FECHA_DE_REMISION'].dt.strftime('%d/%m/%Y')
datos_reg_1427['FECHA_INICIO'] = datos_reg_1427['FECHA_INICIO'].dt.strftime('%d/%m/%Y')
datos_reg_1427['FECHA_FINAL'] = datos_reg_1427['FECHA_FINAL'].dt.strftime('%d/%m/%Y')
datos_reg_1427['FECHA_DE_ENVIO_A_DPE'] = datos_reg_1427['FECHA_DE_ENVIO_A_DPE'].dt.strftime('%d/%m/%Y')
datos_reg_1427['FECHA_DE_RESPUESTA_DPE'] = datos_reg_1427['FECHA_DE_RESPUESTA_DPE'].dt.strftime('%d/%m/%Y')

# Formatear los valores a enteros
datos_reg_1427['DOCUMENTO'] = pd.to_numeric(datos_reg_1427['DOCUMENTO'], errors='coerce')
datos_reg_1427 = datos_reg_1427.dropna(subset=['DOCUMENTO'])
datos_reg_1427['DOCUMENTO'] = datos_reg_1427['DOCUMENTO'].astype(int)

datos_reg_1427['NUMERO_PQR'] = pd.to_numeric(datos_reg_1427['NUMERO_PQR'], errors='coerce')
datos_reg_1427 = datos_reg_1427.dropna(subset=['NUMERO_PQR'])
datos_reg_1427['NUMERO_PQR'] = datos_reg_1427['NUMERO_PQR'].astype(int)

datos_reg_1427['N_NCAPACIDAD_INICIAL'] = pd.to_numeric(datos_reg_1427['N_NCAPACIDAD_INICIAL'], errors='coerce')
datos_reg_1427 = datos_reg_1427.dropna(subset=['N_NCAPACIDAD_INICIAL'])
datos_reg_1427['N_NCAPACIDAD_INICIAL'] = datos_reg_1427['N_NCAPACIDAD_INICIAL'].astype(int)

datos_reg_1427['N_INCAPACIDAD_FINAL'] = pd.to_numeric(datos_reg_1427['N_INCAPACIDAD_FINAL'], errors='coerce')
datos_reg_1427 = datos_reg_1427.dropna(subset=['N_INCAPACIDAD_FINAL'])
datos_reg_1427['N_INCAPACIDAD_FINAL'] = datos_reg_1427['N_INCAPACIDAD_FINAL'].astype(int)
