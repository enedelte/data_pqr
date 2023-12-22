import os
import pandas as pd
import numpy as np
import openpyxl as op
import warnings 
warnings.simplefilter('ignore')

pqr_datos = (r"C:\Users\daale\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS\consolidado.txt")
reg_datos = (r"C:\Users\daale\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS\certificados_1427_PQRS.xlsx")



cert_1427 = pd.read_csv(pqr_datos, sep= ';', encoding="ISO-8859-1", index_col=None, header=0) 
reg_1427 = pd.read_excel(r"C:\Users\daale\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS\certificados_1427_PQRS.xlsx", 
                         sheet_name='CERTIFICADO_PQRS', 
                         header=0)



df = pd.DataFrame(reg_1427)
df = df[['NUMERO_PQR']].sum

print(df)