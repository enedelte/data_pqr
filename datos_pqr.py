import os
import pandas as pd
import numpy as np
import openpyxl as op
import warnings 
warnings.simplefilter('ignore')

#conectores 
pqr_datos = (r"C:\Users\dapache\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS\consolidado.txt")
reg_datos = (r"C:\Users\dapache\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS\certificados_1427_PQRS.xlsx")


#Lectura de datos
cert_1427 = pd.read_csv(pqr_datos, sep= ';', encoding="ISO-8859-1", index_col=None, header=0) 
reg_1427 = pd.read_excel(reg_datos, 
                         sheet_name='CERTIFICADO_PQRS', 
                         header=0)
