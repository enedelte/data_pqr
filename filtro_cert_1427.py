from datos_pqr import cert_1427, reg_1427
import pandas as pd

# Crear DataFrame a partir de cert_1427
datos = pd.DataFrame(cert_1427)

# Poner nombre a la columna de datos

datos.columns = ['Datos']

# Dividir la columna 'Datos' en columnas separadas
datos[['TD', 'Documento', 'Nombre1', 'Nombre2', 'Nombre3', 'Apellido1', 'Apellido2', 'Apellido3']] = datos['Datos'].str.split(' ', expand=True, n=7)

# Filtrar valores nulos y duplicados en 'Documento'
datos_fil = datos[['Documento']].copy()
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
print('Cantidad de Documentos Registrados:', cantidad_registrados)
print('Cantidad de Documentos Repetidos:', cantidad_repetidos)
print('Lista de Documentos Repetidos:\n', conteo_repetidos)
