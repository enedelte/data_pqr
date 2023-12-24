from datos_pqr import cert_1427, reg_1427
import pandas as pd

# Crear DataFrame a partir de cert_1427
datos_cert_1427 = pd.DataFrame(cert_1427)

# Poner nombre a la columna de datos
datos_cert_1427.columns = ['Datos']

# Dividir la columna 'Datos' en columnas separadas
datos_cert_1427[['TD', 'Documento', 'Nombre1', 'Nombre2', 'Nombre3', 'Apellido1', 'Apellido2', 'Apellido3']] = datos_cert_1427['Datos'].str.split(' ', expand=True, n=7)

