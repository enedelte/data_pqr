from datos_pqr import datos_cert_1427, reg_1427
import pandas as pd
import numpy as np



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
print('Cantidad de Documentos Registrados en carpeta de Certificados 1427:\n', cantidad_registrados)
print('Cantidad de Documentos Repetidos en carpeta de Certificados 1427:\n', cantidad_repetidos)
print('Lista de Documentos Repetidos\n en carpeta de Certificados 1427:\n', conteo_repetidos)

# Filtrar valores nulos y duplicados en 'Documento' en Archivo de solicitud Certficados 1427


print('Tabla de registros:\n', reg_1427)


