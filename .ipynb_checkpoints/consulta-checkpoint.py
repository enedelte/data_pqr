from datos_pqr_1427 import datos_cert_1427, reg_1427
import pandas as pd
import numpy as np
import csv


# Filtrar valores nulos y duplicados en 'Documento' en carpeta de Certficados 1427
datos_fil = datos_cert_1427[['Documento']].copy()
datos_fil['Documento'] = datos_fil['Documento'].replace('None', pd.NA)  # Reemplazar 'None' por NaN
datos_fil.dropna(subset=['Documento'], inplace=True)  # Eliminar filas con valores NaN en 'Documento'

# Contar la cantidad de documentos únicos y repetidos
cantidad_registrados = datos_fil['Documento'].count()  # Cantidad de documentos registrados
cantidad_repetidos = datos_fil.duplicated(subset=['Documento']).sum()  # Cantidad de documentos repetidos

# Identificar y contar los documentos repetidos
df_repetidos = datos_fil[datos_fil.duplicated(subset=['Documento'], keep=False)]
conteo_repetidos = df_repetidos['Documento'].value_counts().reset_index()
conteo_repetidos.columns = ['Documento', 'Cantidad']

# Imprimir resultados
# print('Cantidad de Documentos Registrados en carpeta de Certificados 1427:\n', cantidad_registrados)
# print('Cantidad de Documentos Repetidos en carpeta de Certificados 1427:\n', cantidad_repetidos)
# print('Lista de Documentos Repetidos\n en carpeta de Certificados 1427:\n', conteo_repetidos)

# Filtrar valores nulos y duplicados en 'DOCUMENTO' en Archivo de solicitud Certficados 1427
registros = reg_1427[['DOCUMENTO']].copy()
registros['DOCUMENTO'] = registros['DOCUMENTO'].replace('NaN', pd.NA)
registros.dropna(subset=['DOCUMENTO'], inplace=True)  # Eliminar filas con valores NaN en 'Documento
# Contar la cantidad de documentos únicos y repetidos
cantidad_registros = registros['DOCUMENTO'].count()
numero_registros = registros.duplicated(subset=['DOCUMENTO']).sum()
# Identificar y contar los documentos repetidos
registros_repetidos = registros[registros.duplicated(subset=['DOCUMENTO'], keep=False)]
conteo__repetidos = registros_repetidos['DOCUMENTO'].value_counts().reset_index()
conteo__repetidos.columns = ['Documento', 'Cantidad']


# print('Numero de documentos repetidos:\n', numero_registros)
# print('Tabla con numero de documento vs cantidad de registros:\n', conteo__repetidos)

# ruta_reporte = "C:\\Users\\dapache\\OneDrive - NUEVA EPS\\GO_PQR\\"
# with open(ruta_reporte + 'datos_exportados.txt', 'w') as file:
#     file.write(str(numero_registros))
