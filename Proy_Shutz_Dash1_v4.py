#!/usr/bin/env python
# coding: utf-8

# # **PROYECTO SCHUTZ EN PYTHON PARA CREACIÓN DE DASHBOARD 1 - PARTE 1**

# ## 1.- IMPORTACIÓN DE LIBRERÍAS PARA EL PROYECTO

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO
from itertools import zip_longest
import io
import requests
from io import BytesIO
import pandas as pd
import chardet
import re
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from gspread_dataframe import set_with_dataframe
from urllib.request import FancyURLopener
from urllib.request import urlopen
import urllib.request
import xml.etree.ElementTree as ET
import numpy as np
import datetime
import ssl
import warnings
from datetime import datetime, timedelta


# In[2]:


pd.options.display.max_rows = None
pd.options.display.float_format = '{:.2f}'.format

warnings.filterwarnings("ignore", category=FutureWarning, message="Inferring datetime64.*")


# ## 2.- LECTURA DE DATAFRAMES

# ### 2.1 LECTURA "LIBRO MAYOR"

# In[3]:


url = 'http://asp.maximise.cl/query.ashx?alias=gsea&user=excel_bd&password=excel_bd&filename=queries\Libro%20Mayor%202023.txt'

# Descargar el archivo XML desde la URL
with urllib.request.urlopen(url) as response:
    xml_data = response.read()

# Parsear el archivo XML
root = ET.fromstring(xml_data)

# Crear una lista de diccionarios con los datos
data = []
for child in root:
    row = {}
    for subchild in child:
        row[subchild.tag] = subchild.text
    data.append(row)

# Convertir la lista de diccionarios en un dataframe de Pandas
df_libro_mayor = pd.DataFrame(data)

# Imprimir el dataframe
df_libro_mayor.sample(5)


# In[4]:


df_libro_mayor.to_csv('archivos_respaldo/df_libro_mayor_1.csv', index = False)


# ### 2.2 LECTURA "DESPACHOS REALIZADOS"

# In[5]:


url = 'http://asp.maximise.cl/query.ashx?alias=gsea&user=excel_bd&password=excel_bd&filename=queries\Despachos%20Realizados.txt'

# Descargar el archivo XML desde la URL
with urllib.request.urlopen(url) as response:
    xml_data = response.read()

# Parsear el archivo XML
root = ET.fromstring(xml_data)

# Crear una lista de diccionarios con los datos
data = []
for child in root:
    row = {}
    for subchild in child:
        row[subchild.tag] = subchild.text
    data.append(row)

# Convertir la lista de diccionarios en un dataframe de Pandas
df_desp_realizados = pd.DataFrame(data)

# Imprimir el dataframe
df_desp_realizados.sample(5)


# In[6]:


df_desp_realizados.to_csv('archivos_respaldo/df_desp_realizados_1.csv', index = False)


# ### 2.3 LECTURA "CODIGOS DE PROYECTO"

# In[7]:


url = 'http://asp.maximise.cl/query.ashx?alias=gsea&user=excel_bd&password=excel_bd&filename=queries\codigos%20de%20proyectos.txt'

# Descargar el archivo XML desde la URL
with urllib.request.urlopen(url) as response:
    xml_data = response.read()

# Parsear el archivo XML
root = ET.fromstring(xml_data)

# Crear una lista de diccionarios con los datos
data = []
for child in root:
    row = {}
    for subchild in child:
        row[subchild.tag] = subchild.text
    data.append(row)

# Convertir la lista de diccionarios en un dataframe de Pandas
df_cod_proyecto = pd.DataFrame(data)

# Imprimir el dataframe
df_cod_proyecto.sample(5)


# In[8]:


df_cod_proyecto.to_csv('archivos_respaldo/df_cod_proyecto_1.csv', index = False)


# ### 2.4 LECTURA "PROYECTADOS"

# In[9]:


# Se crea un filtro para obtener todos aquellos que tengan valores hasta el MES anterior al mes en curso
import datetime

# Obtener el mes actual de acuerdo a la fecha actual, y el resultado se convierte en el nombre del MES para luego buscar aquel nombre en el archivo.
mes_actual = datetime.date.today().month

print(mes_actual)

if mes_actual == 1:
    mes_actual2 = "ENERO"
elif mes_actual == 2:
    mes_actual2 = "FEBRERO"
elif mes_actual == 3:
    mes_actual2 = "MARZO"
elif mes_actual == 4:
    mes_actual2 = "ABRIL"
elif mes_actual == 5:
    mes_actual2 = "MAYO"
elif mes_actual == 6:
    mes_actual2 = "JUNIO"
elif mes_actual == 7:
    mes_actual2 = "JULIO"
elif mes_actual == 8:
    mes_actual2 = "AGOSTO"
elif mes_actual == 9:
    mes_actual2 = "SEPTIEMBRE"
elif mes_actual == 10:
    mes_actual2 = "OCTUBRE"
elif mes_actual == 11:
    mes_actual2 = "NOVIEMBRE"
else:
    mes_actual2 = "DICIEMBRE"

print(mes_actual2)


# In[10]:


ssl._create_default_https_context = ssl._create_unverified_context

# Lectura de presupuestos desde dropbox
df_proyectado = pd.read_excel("https://www.dropbox.com/s/m96bbvnctgmaxrz/Proyecci%C3%B3n%20mensual%20%282023%29.xlsx?dl=1",sheet_name=mes_actual2 ,engine="openpyxl")
# OJO !! El link original tiene un 0 para ser visto desde la web y un 1 para descargarlo.....
df_proyectado.head(10)


# ### 2.4-2 LECTURA "PROYECTADOS 2"

# In[11]:


# Get the current date
import datetime

fecha_actual = datetime.datetime.now()

# Calculate the previous month
mes_anterior2 = (fecha_actual - timedelta(days=30)).month
print(mes_anterior2)

if mes_anterior2 == 1:
    mes_anterior2 = "ENERO"
elif mes_anterior2 == 2:
    mes_anterior2 = "FEBRERO"
elif mes_anterior2 == 3:
    mes_anterior2 = "MARZO"
elif mes_anterior2 == 4:
    mes_anterior2 = "ABRIL"
elif mes_anterior2 == 5:
    mes_anterior2 = "MAYO"
elif mes_anterior2 == 6:
    mes_anterior2 = "JUNIO"
elif mes_anterior2 == 7:
    mes_anterior2 = "JULIO"
elif mes_anterior2 == 8:
    mes_anterior2 = "AGOSTO"
elif mes_anterior2 == 9:
    mes_anterior2 = "SEPTIEMBRE"
elif mes_anterior2 == 10:
    mes_anterior2 = "OCTUBRE"
elif mes_anterior2 == 11:
    mes_anterior2 = "NOVIEMBRE"
else:
    mes_anterior2 = "DICIEMBRE"

print(mes_anterior2)

# Lectura de presupuestos desde dropbox
df_proyectado_1M = pd.read_excel("https://www.dropbox.com/s/m96bbvnctgmaxrz/Proyecci%C3%B3n%20mensual%20%282023%29.xlsx?dl=1",sheet_name=mes_anterior2 ,engine="openpyxl")
# OJO !! El link original tiene un 0 para ser visto desde la web y un 1 para descargarlo.....
df_proyectado_1M.head(20)


# In[ ]:





# ### 2.5 LECTURA "LIBRO MAYOR AÑOS ANTERIORES"

# In[12]:


# Conexión a google drive

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Credenciales de GOOGLE API, en archivo .json
credentials = ServiceAccountCredentials.from_json_keyfile_name(
         'keen-extension-358919-9214486a06be.json', scope) # Your json file here

gc = gspread.authorize(credentials)

## SIEMPRE DAR ACCESO A ESTE USUARIO: test-321@keen-extension-358919.iam.gserviceaccount.com


# In[13]:


spr = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Fx1nerTu10PZPOwknLcQuri_I6ARat5h7zuq4P3vypg/edit#gid=1097918290')
recipients = spr.sheet1.get_all_values()

# Se el string creado en un dataframe
df_libro_mayor_old = pd.DataFrame(recipients)

# se reasignan los headers en el dataframe.
new_header = df_libro_mayor_old.iloc[0] #grab the first row for the header
df_libro_mayor_old = df_libro_mayor_old[1:] #take the data less the header row
df_libro_mayor_old.columns = new_header #set the header row as the df header

# Se conservan solo las columnas de interés
#df_seguridad_v3 = df_seguridad_v3[["Nº Cédula","Nombres y apellidos","APRUEBA FASE DE CALIFICACIÓN ?","PUNTOS VIGENTES","APRUEBA FASE DE EVALUACIÓN ?","RESULTADO FINAL"]]

print("Las dimensiones del dataframe son :",df_libro_mayor_old.shape)
df_libro_mayor_old.sample(5)


# In[14]:


df_libro_mayor_old.to_csv('archivos_respaldo/df_libro_mayor_old.csv', mode='a')


# ### 2.6 LECTURA "PLANILLA RESUMEN - PRESPUESTOS"

# In[15]:


# Lectura de presupuestos desde dropbox
df_presupuesto = pd.read_excel("https://www.dropbox.com/s/miow7p9wl7t3jsr/PLANILLA%20RESUMEN.xlsb.xlsx?dl=1",sheet_name= "PROYECTOS" ,engine="openpyxl")
# OJO !! El link original tiene un 0 para ser visto desde la web y un 1 para descargarlo.....
df_presupuesto.head(5)


# In[16]:


df_presupuesto.to_csv('archivos_respaldo/df_presupuesto.csv', mode='a')


# In[ ]:





# ### 2.7 LECTURA "TABLA- PRESPUESTOS"

# In[17]:


url = 'http://asp.maximise.cl/query.ashx?alias=gsea&user=excel_bd&password=excel_bd&filename=queries\Presupuesto Proyectos.txt'
response = requests.get(url)
query_result = response.text
soup = BeautifulSoup(response.content, 'xml')
rows = soup.find_all('Table')


data = []
for row in rows:
    values = [cell.text for cell in row.find_all()]
    data.append(values)

df_tabla_prespuesto = pd.DataFrame(data, columns=['CODIGO_PROYECTO','PARTIDA_PRESUPUESTARIA','PRODUCTO','UNIDAD','CANTIDAD','COSTO_UNITARIO','COSTO_TOTAL'])

# Exportación a excel
df_tabla_prespuesto.to_csv('df_tabla_prespuesto.csv', index = False)

df_tabla_prespuesto.head(5)


# ## 3.- TRATAMIENTO DE DATAFRAMES

# ### 3.1 - TRATAMIENTO 1 - LIBRO MAYOR

# #### 3.1.1 - Exploración inicial de los datos

# In[18]:


df_libro_mayor.shape


# In[19]:


df_libro_mayor.info()


# #### 3.1.2 - Estandarización campo "Debito" y Crédito

# In[20]:


# Se crean nuevos campos para trabajar "Debito" y "Credito".

df_libro_mayor['Debito_2'] = pd.to_numeric(df_libro_mayor['Debito'], errors='coerce')
df_libro_mayor['Credito_2'] = pd.to_numeric(df_libro_mayor['Credito'], errors='coerce')

# Se reemplaza el valor de los NoNe y Nan 

df_libro_mayor['Credito_2'] = df_libro_mayor['Credito_2'].fillna(0)

df_libro_mayor.head(5)


# #### 3.1.3 - Creación campo Codigo_proyecto

# In[21]:


# Se crean una nueva columna para manejar el código del proyecto 

df_libro_mayor['Codigo_proyecto'] = df_libro_mayor['Primer_Analisis']

cols = df_libro_mayor.columns.tolist() # Obtiene el nombre de todas las columnas en una lista
cols.insert(0, cols.pop(cols.index('Codigo_proyecto'))) # Extrae la columna 'Codigo_proyecto', la inserta en la posición 0 y actualiza la lista
df_libro_mayor = df_libro_mayor.reindex(columns=cols) # Reindexa el dataframe con las columnas en el orden actualizado

# Transformación a mayúscula código del proyecto
df_libro_mayor['Codigo_proyecto'] = df_libro_mayor['Codigo_proyecto'].str.upper()

df_libro_mayor.head(5)


# #### 3.1.4 - Creación de campo total

# In[22]:


df_libro_mayor['TOTAL'] = df_libro_mayor['Credito_2'] - df_libro_mayor['Debito_2']
df_libro_mayor.head(5)


# #### 3.1.5 - Creación campo tipo_cuenta "basado en el campo cta_Contable"

# In[23]:


# Función para categorizar la columna 'Cta_Contable'
def categorizar_cta_contable(cta_contable):
    if cta_contable =="3101030-000" or cta_contable == "3401002-000":
        return 'INGRESO'
    elif cta_contable == "4101010-000":
        return 'COSTO MATERIALES'
    elif cta_contable == "4150002-000":
        return 'COSTO MANO DE OBRA'
    elif cta_contable == "4150002-002":
        return 'COSTO SUPERVISIÓN'
    else:
        return 'OTRA'

# Crear la nueva columna 'Tipo_cuenta' aplicando la función
df_libro_mayor['Tipo_cuenta'] = df_libro_mayor['Cta_Contable'].apply(categorizar_cta_contable)
df_libro_mayor.sample(5)


# In[24]:


# EXPLORACIÓN DE DATOS

df_libro_mayor_piv = pd.pivot_table(df_libro_mayor, values=['Debito_2','Credito_2','TOTAL'], index=['Tipo_cuenta','Año','Mes'], aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')
df_libro_mayor_piv = pd.DataFrame(df_libro_mayor_piv.to_records())

#df_libro_mayor_piv.head(5)
df_libro_mayor_piv.sample(10)


# #### 3.1.6 - Se eliminan números de proyectos que no deben ser parte del análisis

# In[25]:


# Se crea una copia del dataframe original debido que se reduciran las dimensiones
df_libro_mayor2 = df_libro_mayor.copy()


# In[26]:


# Se identifican los códigos de proyecto disponibles
print("Proyectos disponibles antes de la reducción : ")
print(df_libro_mayor2["Codigo_proyecto"].unique())
print("=======================================================================")
print("Dimensiones del dataframe antes de la reducción : ")
print(df_libro_mayor2.shape)


# ##### 3.1.6.1 - Se Se crea un subdataframe para COSTOS SUPERVISIÓN (separando lo que tiene P-OFICINA y cta_contable 4150002-002)

# In[27]:


# Se crea un dataframe separado para tratar los que poseen proyecto "P-OFICINA" ya que los costos de supervisión solo aplican al total
df_libro_mayor2_2 = df_libro_mayor2.copy()

# Filtrar el DataFrame
df_libro_mayor2_2 = df_libro_mayor2_2[(df_libro_mayor2_2['Codigo_proyecto'] == 'P-OFICINA') & (df_libro_mayor2_2['Cta_Contable'] == '4150002-002')]

# Mostrar el DataFrame filtrado
df_libro_mayor2_2


# In[28]:


# Elimina los registros NaN en la columna Codigo_proyecto
df_libro_mayor2 = df_libro_mayor2.dropna(subset=['Codigo_proyecto'])

# Define una lista de valores a eliminar
valores_a_eliminar = ['P-PROYECTOS', 'P-SERVICIOS','P-OFICINA', 'P-ANALISIS PROYE']

# Crea una máscara booleana que identifica las filas que contienen los valores a eliminar
mask1 = df_libro_mayor2['Codigo_proyecto'].isin(valores_a_eliminar)

# Crea una máscara booleana que identifica las filas que comienzan con un número
mask2 = df_libro_mayor2['Codigo_proyecto'].str[0].str.isnumeric()

# Une las dos máscaras con el operador OR
mask = mask1 | mask2

# Crea un nuevo dataframe sin las filas que contienen los valores a eliminar
df_libro_mayor2 = df_libro_mayor2[~mask]


# Verifica si el valor 'P1718' o valore similares están presentes en la columna Codigo_proyecto
if 'P1718' in df_libro_mayor2['Codigo_proyecto'].values:
    # Reemplaza el valor 'P1718' por 'P-1718' en la columna Codigo_proyecto
    df_libro_mayor2['Codigo_proyecto'] = df_libro_mayor2['Codigo_proyecto'].replace('P1718', 'P-1718')


# In[29]:


# Se identifican los códigos de proyecto disponibles
print("Proyectos disponibles antes de la reducción : ")
print(df_libro_mayor2["Codigo_proyecto"].unique())
print("=======================================================================")
print("Dimensiones del dataframe antes de la reducción : ")
print(df_libro_mayor2.shape)


# #### 3.1.7 - Se crea un nuevo campo de fecha basado en la fecha original

# In[30]:


df_libro_mayor2['Fecha2'] = pd.to_datetime(df_libro_mayor2['Año'].astype(str) + '-' + df_libro_mayor2['Mes'].astype(str) + '-1')
df_libro_mayor2.sample(5)


# ##### 3.1.7.1 - Se crea un nuevo campo de fecha basado en la fecha original para  COSTOS SUPERVISIÓN

# In[31]:


df_libro_mayor2_2['Fecha2'] = pd.to_datetime(df_libro_mayor2_2['Año'].astype(str) + '-' + df_libro_mayor2_2['Mes'].astype(str) + '-1')
df_libro_mayor2_2.sample(5)


# #### 3.1.8 - Se realiza pivote final del dataframe

# In[32]:


# Se exploran las columnas:
df_libro_mayor2.columns


# In[33]:


# crear pivot table sin margenes

df_libro_mayor2_piv = pd.pivot_table(df_libro_mayor2, values=['Debito_2','Credito_2','TOTAL'], index=['Codigo_proyecto','Tipo_cuenta','Fecha2','Año','Mes'], aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')
df_libro_mayor2_piv = pd.DataFrame(df_libro_mayor2_piv.to_records())

df_libro_mayor2_piv.sample(5)


# In[34]:


# Estas son las dimensiones del dataframe pivoteado:
df_libro_mayor2_piv.shape


# ##### 3.1.8.1 - Se realiza pivote final del dataframe paera COSTO SUPERVISIÓN

# In[35]:


# crear pivot table sin margenes

df_libro_mayor2_2_piv = pd.pivot_table(df_libro_mayor2_2, values=['Debito_2','Credito_2','TOTAL'], index=['Codigo_proyecto','Tipo_cuenta','Fecha2','Año','Mes'], aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')
df_libro_mayor2_2_piv = pd.DataFrame(df_libro_mayor2_2_piv.to_records())

df_libro_mayor2_2_piv = df_libro_mayor2_2_piv[df_libro_mayor2_2_piv['Codigo_proyecto'] != 'TOTAL']

# Se reemplaza el valor P-OFICINA por el valor TOTAL con lo cual se utilizará para unirlo al dataframe que crea las filas para el cálculo de los totales
df_libro_mayor2_2_piv['Codigo_proyecto'] = df_libro_mayor2_2_piv['Codigo_proyecto'].replace('P-OFICINA', 'TOTAL')


df_libro_mayor2_2_piv


# #### 3.1.9 - Se crea subdataframe para proyecto que considera el total con nombre "TOTAL", que se detalla por tipo_cuenta

# In[36]:


df_libro_mayor_piv2 = pd.pivot_table(df_libro_mayor2_piv, values=['Debito_2','Credito_2','TOTAL'], index=['Tipo_cuenta','Fecha2','Año','Mes'], aggfunc='sum', fill_value=0)
df_libro_mayor_piv2 = pd.DataFrame(df_libro_mayor_piv2.to_records())

# Agregamos la columna Codigo_proyecto con valor "TOTAL" en la primera columna
df_libro_mayor_piv2.insert(loc=0, column='Codigo_proyecto', value='TOTAL')

# Eliminamos los registros con Tipo_cuenta igual a "TOTAL"
df_libro_mayor_piv2 = df_libro_mayor_piv2[df_libro_mayor_piv2['Tipo_cuenta'] != 'TOTAL']
df_libro_mayor_piv2 = df_libro_mayor_piv2[df_libro_mayor_piv2['Tipo_cuenta'] != '']

df_libro_mayor_piv2


# ##### 3.1.9.1 - Se anexa el dataframe creado con los totales con el dataframe creado a partir del punto 3.1.6.1 que contiene los costos de supervisión

# In[37]:


df_libro_mayor_piv2 = pd.concat([df_libro_mayor_piv2, df_libro_mayor2_2_piv], ignore_index=True)
df_libro_mayor_piv2


# #### 3.1.10 - Se concatenan los 2 dataframes resultantes

# In[38]:


print("=======================================================================")
print("Dimensiones del dataframe antes de la concatenación : ")
print(df_libro_mayor2_piv.shape)


# In[39]:


df_libro_mayor3 = pd.concat([df_libro_mayor2_piv, df_libro_mayor_piv2])
df_libro_mayor3.sort_values(by=['Codigo_proyecto']).sample(5)


# In[40]:


print("=======================================================================")
print("Dimensiones del dataframe después de la concatenación : ")
print(df_libro_mayor3.shape)


# #### 3.1.11 - Se crean las filas que permiten tener siempre todas las opciones de Tipo_Cuenta por cada Codigo_proyecto

# In[41]:


combinaciones = []
for proyecto in df_libro_mayor3['Codigo_proyecto'].unique():
    for fecha in df_libro_mayor3['Fecha2'].unique():
        mes = pd.to_datetime(fecha).month
        año = pd.to_datetime(fecha).year
        for cuenta in ['INGRESO', 'COSTO MATERIALES', 'COSTO MANO DE OBRA', 'COSTO SUPERVISIÓN']:
            combinaciones.append((proyecto, fecha, mes, año, cuenta))

# crear un nuevo DataFrame con las combinaciones obtenidas
combinaciones_df = pd.DataFrame(combinaciones, columns=['Codigo_proyecto', 'Fecha2', 'Mes', 'Año', 'Tipo_cuenta'])

# agregar las demás columnas con valores nulos
combinaciones_df['Credito_2'] = 0
combinaciones_df['Debito_2'] = 0
combinaciones_df['TOTAL'] = 0

# Se eliminan filas con fecha en blanco.
combinaciones_df = combinaciones_df.dropna(subset=['Mes'])

combinaciones_df.sample(10)


# #### 3.1.12 - Se concatenan los 2 dataframes resultantes

# In[42]:


print("=======================================================================")
print("Dimensiones del dataframe antes de la concatenación : ")
print(df_libro_mayor3.shape)


# In[43]:


df_libro_mayor4 = pd.concat([df_libro_mayor3, combinaciones_df])
df_libro_mayor4.sort_values(by=['Codigo_proyecto']).sample(5)


# In[44]:


print("=======================================================================")
print("Dimensiones del dataframe después de la concatenación : ")
print(df_libro_mayor4.shape)


# #### 3.1.13 - Estandarización de campos 

# In[45]:


# Se estandarizan los campos con sus nombres y formatos, para un mayor entendimiento.

df_libro_mayor4 = df_libro_mayor4.rename(columns={
    'Codigo_proyecto': 'CODIGO_PROYECTO',
    'Tipo_cuenta': 'TIPO_CUENTA',
    'Fecha2': 'FECHA',
    'Año': 'AÑO',
    'Mes': 'MES',
    'Credito_2': 'CREDITO',
    'Debito_2': 'DEBITO'
})

df_libro_mayor4['AÑO'] = pd.to_numeric(df_libro_mayor4['AÑO'], downcast='integer')
df_libro_mayor4['MES'] = pd.to_numeric(df_libro_mayor4['MES'], downcast='integer')

df_libro_mayor4.sample(10)


# In[46]:


#df_libro_mayor4[df_libro_mayor4["CODIGO_PROYECTO"]=="P-1706"]
df_libro_mayor4[df_libro_mayor4["CODIGO_PROYECTO"]=="TOTAL"]


# #### 3.1.14 Creación de columna MARGEN

# In[47]:


df_libro_mayor4_2 = df_libro_mayor4.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_libro_mayor4_2.groupby(['CODIGO_PROYECTO','MES']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

    
df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(5)


# In[48]:


print("=======================================================================")
print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor4_2  : ", df_libro_mayor4.shape)
print("=======================================================================")
print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_margen          : ", df_margen.shape)
print(df_margen.shape)


# In[49]:


# CONCATENACIÓN DE DATAFRAMES

df_libro_mayor5 = pd.merge(df_libro_mayor4, df_margen, on=['CODIGO_PROYECTO', 'MES'], how='left')

# Se estandariza el valor TOTAL a 1.TOTAL para que pueda ser seleccionado desde los filtros del Dashboard.
df_libro_mayor5['CODIGO_PROYECTO'] = df_libro_mayor5['CODIGO_PROYECTO'].apply(lambda x: '1. TOTAL' if x == 'TOTAL' else x)

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5  : ", df_libro_mayor5.shape)
print(df_libro_mayor5.shape)


# In[50]:


# INSPECCIÓN VISUAL 1
df_libro_mayor5[df_libro_mayor5["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[51]:


# INSPECCIÓN VISUAL 2
df_libro_mayor5[df_libro_mayor5["CODIGO_PROYECTO"]=="P-1704"]


# In[52]:


df_libro_mayor5["CODIGO_PROYECTO"].unique()


# In[53]:


df_libro_mayor5.to_csv('archivos_respaldo/df_libro_mayor5.csv', index = False)


# In[ ]:





# ### 3.1 - TRATAMIENTO 1 - LIBRO MAYOR SUBSETS

# #### 3.1.16 - CREACIÓN DF **"YTD AÑO EN CURSO HASTA MES CERRADO"**

# In[54]:


fecha_actual = datetime.date.today()
fecha_actual


# In[55]:


# Se crea una copia del dataframe 

df_libro_mayor_ytd = df_libro_mayor5.copy()
df_libro_mayor_ytd.sample(5)


# In[56]:


# Se crea un filtro para obtener todos aquellos que tengan valores hasta el MES anterior al mes en curso

# Obtener el mes actual
mes_actual = datetime.date.today().month
print(mes_actual)

# Filtrar los registros del dataframe que corresponden al mes actual y a todos los meses anteriores
df_libro_mayor_ytd["FECHA"] = pd.to_datetime(df_libro_mayor_ytd["FECHA"])
df_libro_mayor_ytd_closed = df_libro_mayor_ytd[df_libro_mayor_ytd["FECHA"].dt.month < mes_actual]

df_libro_mayor_ytd_closed.sample(10)


# In[57]:


# crear pivot table sin margenes

df_libro_mayor_ytd_closed_piv = pd.pivot_table(df_libro_mayor_ytd_closed, values=['TOTAL'], index=['CODIGO_PROYECTO', 'TIPO_CUENTA'], aggfunc='sum', fill_value=0)
#df_libro_mayor4_piv = pd.pivot_table(df_libro_mayor4, values=['Debito_2','Credito_2','TOTAL'], index=['Codigo_proyecto','Tipo_cuenta'], columns = ['Fecha2'], aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')

df_libro_mayor_ytd_closed_piv = pd.DataFrame(df_libro_mayor_ytd_closed_piv.to_records())

df_libro_mayor_ytd_closed_piv.sample(10)


# #### 3.1.16-1 - CREACIÓN DF **"YTD AÑO EN CURSO HASTA MES CERRADO 2"**
# Este dataframe es para considerar como mes cerrado 2 meses atrás, de esta forma se puede evaluar el mes cerrado.

# In[58]:


# Obtener el mes actual
mes_actual = datetime.date.today().month
print(mes_actual)

# Calcular el mes que es dos meses antes del actual
mes_filtrado = mes_actual - 2 if mes_actual > 2 else (12 + mes_actual - 2) 

# Filtrar los registros del dataframe que corresponden al mes filtrado y a todos los meses anteriores
df_libro_mayor_ytd["FECHA"] = pd.to_datetime(df_libro_mayor_ytd["FECHA"])
df_libro_mayor_ytd_closed_2M = df_libro_mayor_ytd[df_libro_mayor_ytd["FECHA"].dt.month <= mes_filtrado]

df_libro_mayor_ytd_closed_2M.sample(10)


# In[59]:


# crear pivot table sin margenes

df_libro_mayor_ytd_closed_2M = pd.pivot_table(df_libro_mayor_ytd_closed_2M, values=['TOTAL'], index=['CODIGO_PROYECTO', 'TIPO_CUENTA'], aggfunc='sum', fill_value=0)

df_libro_mayor_ytd_closed_2M = pd.DataFrame(df_libro_mayor_ytd_closed_2M.to_records())

df_libro_mayor_ytd_closed_2M.sample(5)


# #### 3.1.17 - CREACIÓN DF **LIBRO MAYOR PARA MES EN CURSO**

# In[60]:


# Se crea un nuevo dataframe basado en df_libro_mayor5, la palabra "mec" significa mes en curso.
 
df_libro_mayor5_mec = df_libro_mayor5.copy()
df_libro_mayor5_mec.shape
print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_mec  : ", df_libro_mayor5_mec.shape)
df_libro_mayor5_mec.sample(3)


# In[61]:


# Se crea una nueva columna para categorizar el origen de los datos.

df_libro_mayor5_mec["ORIGEN"]="LIBRO MAYOR"
df_libro_mayor5_mec.sample(5)


# In[62]:


# Se seleccionan los meses que son utiles para crear la vista de mes en curso.
# Para el real se necesita: INGRESO, COSTO MATERIALES, Y SUPERVISIÓN (ÉSTE ÚLTIMO DEL MES ANTERIOR)
# Para el proyectado se necesita: SUPERVISIÓN (DEL MES ANTERIOR)


# In[63]:


# Filtro para TIPO_CUENTA y FECHA
from datetime import datetime, timedelta


df_libro_mayor5_mec['FECHA'] = pd.to_datetime(df_libro_mayor5_mec['FECHA'])

filtro_ingreso_materiales = ((df_libro_mayor5_mec['TIPO_CUENTA'] == 'INGRESO') | 
                             (df_libro_mayor5_mec['TIPO_CUENTA'] == 'COSTO MATERIALES')) & \
                            (df_libro_mayor5_mec['FECHA'].dt.month == datetime.now().month)

# Filtro para SUPERVISIÓN del mes anterior
mes_anterior = (datetime.now() - timedelta(days=32)).month
filtro_supervision_mes_anterior = (df_libro_mayor5_mec['TIPO_CUENTA'] == 'COSTO SUPERVISIÓN') & \
                                  (df_libro_mayor5_mec['FECHA'].dt.month == mes_anterior)


# Filtro para COSTO_MANO_OBRA del mes anterior
mes_anterior = (datetime.now() - timedelta(days=32)).month
filtro_mo_mes_anterior = (df_libro_mayor5_mec['TIPO_CUENTA'] == 'COSTO MANO DE OBRA') & \
                                  (df_libro_mayor5_mec['FECHA'].dt.month == mes_anterior)

# Combinar los filtros en un filtro general
filtro_general = filtro_ingreso_materiales | filtro_supervision_mes_anterior  | filtro_mo_mes_anterior

# Crear el sub-dataframe filtrado
df_libro_mayor5_mec2 = df_libro_mayor5_mec[filtro_general]

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_mec2  : ", df_libro_mayor5_mec2.shape)

df_libro_mayor5_mec2.sample(10)


# In[64]:


# INSPECCIÓN VISUAL 1
df_libro_mayor5_mec2[df_libro_mayor5_mec2["CODIGO_PROYECTO"]=="P-1704"]


# In[65]:


# INSPECCIÓN VISUAL 2
df_libro_mayor5_mec2[df_libro_mayor5_mec2["CODIGO_PROYECTO"]=="1. TOTAL"]


# #### 3.1.17-1 - CREACIÓN DF **LIBRO MAYOR PARA MES EN CURSO 2**
# Este dataframe es para considerar como mes en curso de 2 meses atrás, de esta forma se puede evaluar el mes cerrado.

# In[66]:


# Se crea un nuevo dataframe basado en df_libro_mayor5, la palabra "mec" significa mes en curso.

df_libro_mayor5_mec_2M = df_libro_mayor5.copy()
df_libro_mayor5_mec_2M.shape
print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_mec_2M  : ", df_libro_mayor5_mec_2M.shape)
df_libro_mayor5_mec_2M.sample(3)


# In[67]:


# Se crea una nueva columna para categorizar el origen de los datos.

df_libro_mayor5_mec_2M["ORIGEN"]="LIBRO MAYOR"
df_libro_mayor5_mec_2M.sample(5)


# In[68]:


# Filtro para TIPO_CUENTA y FECHA
from datetime import datetime, timedelta

df_libro_mayor5_mec_2M['FECHA'] = pd.to_datetime(df_libro_mayor5_mec_2M['FECHA'])

# Filtro para INGRESO Y COSTO DE MATERIALES
mes_anterior = (datetime.now() - timedelta(days=30)).month

filtro_ingreso_materiales = ((df_libro_mayor5_mec_2M['TIPO_CUENTA'] == 'INGRESO') | 
                             (df_libro_mayor5_mec_2M['TIPO_CUENTA'] == 'COSTO MATERIALES')) & \
                            (df_libro_mayor5_mec_2M['FECHA'].dt.month == mes_anterior)

# Filtro para SUPERVISIÓN del mes anterior
mes_anterior2 = (datetime.now() - timedelta(days=60)).month

filtro_supervision_mes_anterior = (df_libro_mayor5_mec_2M['TIPO_CUENTA'] == 'COSTO SUPERVISIÓN') & \
                                  (df_libro_mayor5_mec_2M['FECHA'].dt.month == mes_anterior2)


# Filtro para COSTO_MANO_OBRA del mes anterior
mes_anterior2 = (datetime.now() - timedelta(days=60)).month

filtro_mo_mes_anterior = (df_libro_mayor5_mec_2M['TIPO_CUENTA'] == 'COSTO MANO DE OBRA') & \
                                  (df_libro_mayor5_mec_2M['FECHA'].dt.month == mes_anterior2)

# Combinar los filtros en un filtro general
filtro_general = filtro_ingreso_materiales | filtro_supervision_mes_anterior  | filtro_mo_mes_anterior

# Crear el sub-dataframe filtrado
df_libro_mayor5_mec_2M = df_libro_mayor5_mec_2M[filtro_general]

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_mec_2M  : ", df_libro_mayor5_mec_2M.shape)

df_libro_mayor5_mec_2M.sample(5)


# In[69]:


# INSPECCIÓN VISUAL 1
df_libro_mayor5_mec_2M[df_libro_mayor5_mec_2M["CODIGO_PROYECTO"]=="P-1704"]


# In[70]:


# INSPECCIÓN VISUAL 2
df_libro_mayor5_mec_2M[df_libro_mayor5_mec_2M["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[ ]:





# #### 3.1.18 - CREACIÓN DF **LIBRO MAYOR PARA YTD MES PROYECTADO (Incluyendo mes actual)**

# In[71]:


# Se crea una copia del dataframe 

df_libro_mayor_ytd2 = df_libro_mayor5.copy()
df_libro_mayor_ytd2.sample(10)


# In[72]:


# crear pivot table sin margenes

df_libro_mayor_ytd2_closed_piv = pd.pivot_table(df_libro_mayor_ytd2, values=['TOTAL'], index=['CODIGO_PROYECTO', 'TIPO_CUENTA'], aggfunc='sum', fill_value=0)

df_libro_mayor_ytd2_closed_piv = pd.DataFrame(df_libro_mayor_ytd2_closed_piv.to_records())

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor_ytd2_closed_piv  : ", df_libro_mayor_ytd2_closed_piv.shape)

df_libro_mayor_ytd2_closed_piv.sample(10)


# #### 3.1.18-2 - CREACIÓN DF **LIBRO MAYOR PARA YTD MES PROYECTADO (Incluyendo mes actual) 2**

# In[73]:


# Obtener el mes actual
mes_actual = datetime.now().month

# Filtrar los registros hasta el mes anterior al mes actual
df_libro_mayor_ytd2_1M = df_libro_mayor_ytd2[df_libro_mayor_ytd2['MES'] < mes_actual]

# Mostrar el nuevo DataFrame
print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor_ytd2_1M  : ", df_libro_mayor_ytd2_1M.shape)
df_libro_mayor_ytd2_1M.sample(5)


# In[74]:


# crear pivot table sin margenes

df_libro_mayor_ytd2_closed_piv_1M = pd.pivot_table(df_libro_mayor_ytd2_1M, values=['TOTAL'], index=['CODIGO_PROYECTO', 'TIPO_CUENTA'], aggfunc='sum', fill_value=0)

df_libro_mayor_ytd2_closed_piv_1M = pd.DataFrame(df_libro_mayor_ytd2_closed_piv_1M.to_records())

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor_ytd2_closed_piv_1M  : ", df_libro_mayor_ytd2_closed_piv_1M.shape)

df_libro_mayor_ytd2_closed_piv_1M.sample(10)


# #### 3.1.19 - CREACIÓN DE DATAFRAME BASE LIBRO MAYOR 2023 PARA EL CRUCE OTROS DATAFRAMES

# ##### NOTA IMPORTANTE
# ##### Se considera que todos los dataframes que pintan los dashboards deben tener como base los proyectos abiertos en el Libro Mayor 2023. Para esto se crea el dataframe base con el cual debe comenzar cualquier cruce de datos y que considera el código del proyecto, todos los tipos de cuenta por cada proyecto y con valor en cero, además se cruza con la tabla codigo de proyecto.

# In[75]:


df_libro_mayor5_base = df_libro_mayor5.copy()


# In[76]:


print(df_libro_mayor5_base["CODIGO_PROYECTO"].unique())

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_libro_mayor5_base   : ", df_libro_mayor5_base.shape)

df_libro_mayor5_base = df_libro_mayor5_base[['CODIGO_PROYECTO','TIPO_CUENTA']].drop_duplicates()

# Se elimina fila de TOTAL
df_libro_mayor5_base = df_libro_mayor5_base[df_libro_mayor5_base['CODIGO_PROYECTO'] != '1. TOTAL']

# Se Reemplazan valores de la column TIPO_CUENTA
df_libro_mayor5_base['TIPO_CUENTA'] = df_libro_mayor5_base['TIPO_CUENTA'].replace({
    'INGRESO': '1. INGRESO',
    'COSTO MATERIALES': '2. COSTO MATERIALES',
    'COSTO MANO DE OBRA': '3. COSTO MANO DE OBRA',
    'COSTO SUPERVISIÓN': '4. COSTO SUPERVISIÓN'
})

df_libro_mayor5_base['TOTAL_LB']= 0

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_libro_mayor5_base : ", df_libro_mayor5_base.shape)
df_libro_mayor5_base.sample(10)


# In[77]:


# Se Agrega COSTO DE SUPERVISIÓN

nueva_fila = pd.DataFrame({'CODIGO_PROYECTO': ['1. TOTAL'],
                           'TIPO_CUENTA': ['4. COSTO SUPERVISIÓN'],
                           'TOTAL_LB': [0]})

df_libro_mayor5_base = pd.concat([df_libro_mayor5_base, nueva_fila], ignore_index=True)

df_libro_mayor5_base[df_libro_mayor5_base["CODIGO_PROYECTO"]=="1. TOTAL"]
print(df_libro_mayor5_base["CODIGO_PROYECTO"].unique())
print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_libro_mayor5_base : ", df_libro_mayor5_base.shape)


# In[78]:


# Crear DataFrame con TIPO_CUENTA y valor cero para cada combinación única

df_nuevo = pd.DataFrame({
    'CODIGO_PROYECTO': df_libro_mayor5_base['CODIGO_PROYECTO'].repeat(4),
    'TIPO_CUENTA': ['1. INGRESO', '2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN'] * len(df_libro_mayor5_base),
    'TOTAL_LB': 0
})

print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_libro_mayor5_base : ", df_libro_mayor5_base.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_nuevo             : ", df_nuevo.shape)

df_libro_mayor5_base = pd.concat([df_libro_mayor5_base, df_nuevo], ignore_index=True)

# Se remueve cualquier duplicado.
df_libro_mayor5_base.drop_duplicates(inplace=True)

print("DIMENSIONES ANTERIOR DESPUÉS DE CAMBIOS DATAFRAME: df_libro_mayor5_base : ", df_libro_mayor5_base.shape)
df_libro_mayor5_base.sample(5)


# In[79]:


# INSPECCIÓN VISUAL 1
df_libro_mayor5_base.sort_values(by=['CODIGO_PROYECTO','TIPO_CUENTA']).head(10)


# In[80]:


# MERGE CON CODIGO_PROYECTO

# Se crea dataframe de codigos de proyecto y se aplica mayúscula
df_cod_proyecto_base = df_cod_proyecto.applymap(lambda s: s.upper() if isinstance(s, str) else s)

# Se hace merge con los codigos de proyecto.

print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_libro_mayor5_base : ", df_libro_mayor5_base.shape)

df_libro_mayor5_base2 = pd.merge(df_libro_mayor5_base, df_cod_proyecto_base, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_libro_mayor5_base : ", df_libro_mayor5_base.shape)

df_libro_mayor5_base2.sample(10)


# In[81]:


# Modificar las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" para "1. TOTAL"

df_libro_mayor5_base2.loc[df_libro_mayor5_base2['CODIGO_PROYECTO'] == '1. TOTAL', ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

df_libro_mayor5_base2.sample(10) 


# In[82]:


# INSPECCIÓN VISUAL 1

df_libro_mayor5_base2[df_libro_mayor5_base2['CODIGO_PROYECTO']=="1. TOTAL"]


# In[83]:


# INSPECCIÓN VISUAL 2

df_libro_mayor5_base2[df_libro_mayor5_base2['CODIGO_PROYECTO']=="P-1704"]


# ### 3.2 - TRATAMIENTO DE DESPACHOS REALIZADOS

# #### 3.2.1 - Creación de dataframe copia

# In[84]:


df_desp_realizados2 = df_desp_realizados.copy()
df_desp_realizados2.head(5)


# #### 3.2.2 - Se eliminan proyectos relacionados a STT, P-Proyectos, P-Servicios, P-Mantención

# In[85]:


df_desp_realizados2["COD_PROYECTO"].unique()


# In[86]:


valores_eliminar = ['STT', 'P-Proyectos', 'P-Servicios', 'P-Mantención','P-Oficina''P-ANALISIS PROYE','P-ANALISIS PROYE','P-PROYECTOS','P-Oficina','nan']

# Convertir los valores a eliminar y la columna 'PROYECTO' a mayúsculas
valores_eliminar_mayusculas = [valor.upper() for valor in valores_eliminar]
df_desp_realizados2['PROYECTO_MAYUS'] = df_desp_realizados2['COD_PROYECTO'].str.upper()

# Filtrar las filas que no contengan los valores a eliminar
df_desp_realizados3 = df_desp_realizados2[~df_desp_realizados2['PROYECTO_MAYUS'].isin(valores_eliminar_mayusculas)]

# Eliminar la columna auxiliar 'PROYECTO_MAYUS'
df_desp_realizados3 = df_desp_realizados3.drop(columns=['PROYECTO_MAYUS'])

df_desp_realizados3.sample(10)


# #### 3.2.2 - Se eliminan Tipos de movimientos diferentes a VCO y GDP

# In[87]:


# Reemplazar los valores NaN en la columna "TIPO MOVIMIENTO" con una cadena vacía
df_desp_realizados3['TIPO_x0020_MOVIMIENTO'] = df_desp_realizados3['TIPO_x0020_MOVIMIENTO'].fillna('')

# Filtrar las filas donde "TIPO MOVIMIENTO" sea igual a "VCO" o "GDP" y excluir otros valores

mask = df_desp_realizados3['TIPO_x0020_MOVIMIENTO'].isin(['VCO', 'GDP'])
df_desp_realizados3 = df_desp_realizados3[mask]


# In[88]:


# Se realiza la evaluación de dimensiones después de la eliminación de filas
print("\nDataframe Original antes de los cambios:")
print(df_desp_realizados.shape)
print("Dataframe después de eliminar registros:")
print(df_desp_realizados3.shape)

df_desp_realizados3.to_csv('df_desp_realizados3.csv', index = False)


# In[89]:


# Convertir la columna 'FECHA GUIA' a objetos de fecha y hora, manejando campos en blanco o no válidos como fechas
df_desp_realizados3['FECHA GUIA 2'] = pd.to_datetime(df_desp_realizados3['FECHA_x0020_GUIA'], errors='coerce')

# Extraer el MES y el AÑO en nuevas columnas utilizando funciones lambda y apply()
df_desp_realizados3['MES'] = df_desp_realizados3['FECHA GUIA 2'].apply(lambda x: x.month if pd.notnull(x) else None)
df_desp_realizados3['AÑO'] = df_desp_realizados3['FECHA GUIA 2'].apply(lambda x: x.year if pd.notnull(x) else None)

df_desp_realizados3.sample(5)


# #### 3.2.4 - Se realizan tablas pivot

# In[90]:


df_desp_realizados3['COSTO_x0020_TOTAL'] = df_desp_realizados3['COSTO_x0020_TOTAL'].astype(int)
df_desp_realizados3['CANTIDAD'] = df_desp_realizados3['CANTIDAD'].astype(float)


# In[91]:


df_desp_realizados3.columns


# In[92]:


# Crear el pivot dataframe
df_desp_realizados4 = pd.pivot_table(df_desp_realizados3, 
                          values=['CANTIDAD', 'COSTO_x0020_TOTAL'], 
                          index=['COD_PROYECTO', 'AÑO', 'MES'], 
                          aggfunc='sum', 
                          columns='TIPO_x0020_MOVIMIENTO')

df_desp_realizados4 = pd.DataFrame(df_desp_realizados4.to_records())

df_desp_realizados4.sample(10)


# #### 3.2.5 - Se renombran columnas 

# In[93]:


df_desp_realizados4 = df_desp_realizados4.rename(columns={'COD_PROYECTO': 'CODIGO_PROYECTO'})
df_desp_realizados4 = df_desp_realizados4.rename(columns={"('CANTIDAD', 'GDP')": "CANT. GDP"})
df_desp_realizados4 = df_desp_realizados4.rename(columns={"('CANTIDAD', 'VCO')": "CANT. VCO"})
df_desp_realizados4 = df_desp_realizados4.rename(columns={"('COSTO_x0020_TOTAL', 'GDP')": "TOTAL. GDP"})
df_desp_realizados4 = df_desp_realizados4.rename(columns={"('COSTO_x0020_TOTAL', 'VCO')": "TOTAL. VCO"})

df_desp_realizados4.sample(5)


# #### 3.2.6 - Se reemplazas columnas NaN por ceros y se crea columna de TOTAL GPD-VCO

# In[94]:


df_desp_realizados4.fillna(0, inplace=True)
df_desp_realizados4['TOTAL. VCO - GDP'] = df_desp_realizados4['TOTAL. VCO'] - df_desp_realizados4['TOTAL. GDP']
df_desp_realizados4.sample(5)


# #### 3.2.7 - Se seleccionan solamente los registros del mes y año en curso 

# In[95]:


# Obtener el año y mes actual
#now = datetime.datetime.now()

now = datetime.now()
current_year = now.year
print(current_year)
current_month = now.month
print(current_month)
print("Dimensiones antes del filtro", df_desp_realizados4.shape)

# Filtrar el dataframe por año y mes
df_desp_realizados5 = df_desp_realizados4[(df_desp_realizados4['AÑO'] == current_year) & (df_desp_realizados4['MES'] == current_month)]
print("Dimensiones después del filtro", df_desp_realizados5.shape)
df_desp_realizados5.sample(5)


# #### 3.2.7-2 - Se seleccionan solamente los registros del mes y año en curso 2
# Se considera esta línea para poblar la vista del mes anterior.

# In[96]:


# Obtener el año y mes actual
#now = datetime.datetime.now()

now = datetime.now()
current_year = now.year
print(current_year)
current_month = now.month
print(current_month)
print("Dimensiones antes del filtro", df_desp_realizados4.shape)

mes_anterior = (datetime.now() - timedelta(days=30)).month

# Filtrar el dataframe por año y mes
df_desp_realizados5_1M = df_desp_realizados4[(df_desp_realizados4['AÑO'] == current_year) & (df_desp_realizados4['MES'] == mes_anterior)]
print("Dimensiones después del filtro", df_desp_realizados5_1M.shape)
df_desp_realizados5_1M.sample(5)


# In[ ]:





# #### 3.2.8 - Se agrega la fila TOTAL

# In[97]:


# Obtener la suma de cada columna y guardarla en un diccionario

print("Dimensiones antes del filtro", df_desp_realizados5.shape)

total_row = {
    'CODIGO_PROYECTO': 'TOTAL',
    'AÑO': df_desp_realizados5['AÑO'].iloc[0], # Obtener el valor del año de la primera fila
    'MES': df_desp_realizados5['MES'].iloc[0], # Obtener el valor del mes de la primera fila
    'CANT. GDP': df_desp_realizados5['CANT. GDP'].sum(),
    'CANT. VCO': df_desp_realizados5['CANT. VCO'].sum(),
    'TOTAL. GDP': df_desp_realizados5['TOTAL. GDP'].sum(),
    'TOTAL. VCO': df_desp_realizados5['TOTAL. VCO'].sum(),
    'TOTAL. VCO - GDP': df_desp_realizados5['TOTAL. VCO - GDP'].sum()
}

total_df = pd.DataFrame(total_row, index=[0]) # Crear un nuevo DataFrame con la fila 'TOTAL'
df_desp_realizados5 = pd.concat([df_desp_realizados5, total_df], ignore_index=True) # Concatenar el nuevo DataFrame con el original

#df_desp_realizados5["TIPO_CUENTA"]= df_desp_realizados5["TOTAL. VCO - GDP"]
df_desp_realizados5["TOTAL"]= df_desp_realizados5["TOTAL. VCO - GDP"]
df_desp_realizados5["TIPO_CUENTA"]= "COSTO MATERIALES"

df_desp_realizados5.sample()

print("Dimensiones después del filtro", df_desp_realizados5.shape)

df_desp_realizados5.sample(5)


# #### 3.2.8-2 - Se agrega la fila TOTAL 2

# In[98]:


# Obtener la suma de cada columna y guardarla en un diccionario

print("Dimensiones antes del filtro", df_desp_realizados5_1M.shape)

total_row = {
    'CODIGO_PROYECTO': 'TOTAL',
    'AÑO': df_desp_realizados5_1M['AÑO'].iloc[0], # Obtener el valor del año de la primera fila
    'MES': df_desp_realizados5_1M['MES'].iloc[0], # Obtener el valor del mes de la primera fila
    'CANT. GDP': df_desp_realizados5_1M['CANT. GDP'].sum(),
    'CANT. VCO': df_desp_realizados5_1M['CANT. VCO'].sum(),
    'TOTAL. GDP': df_desp_realizados5_1M['TOTAL. GDP'].sum(),
    'TOTAL. VCO': df_desp_realizados5_1M['TOTAL. VCO'].sum(),
    'TOTAL. VCO - GDP': df_desp_realizados5_1M['TOTAL. VCO - GDP'].sum()
}

total_df = pd.DataFrame(total_row, index=[0]) # Crear un nuevo DataFrame con la fila 'TOTAL'
df_desp_realizados5_1M = pd.concat([df_desp_realizados5_1M, total_df], ignore_index=True) # Concatenar el nuevo DataFrame con el original

#df_desp_realizados5["TIPO_CUENTA"]= df_desp_realizados5["TOTAL. VCO - GDP"]
df_desp_realizados5_1M["TOTAL"]= df_desp_realizados5_1M["TOTAL. VCO - GDP"]
df_desp_realizados5_1M["TIPO_CUENTA"]= "COSTO MATERIALES"

print("Dimensiones después del filtro", df_desp_realizados5_1M.shape)

df_desp_realizados5_1M.sample(5)


# In[99]:


df_desp_realizados5.to_csv('archivos_respaldo/df_desp_realizados5.csv', mode='a')
df_desp_realizados5_1M.to_csv('archivos_respaldo/df_desp_realizados5_1M.csv', mode='a')


# ### 3.4 TRATAMIENTO "PROYECTADO"

# #### 3.4.1 CREACIÓN NUEVO DATAFRAME DE COPIA.

# In[100]:


df_proyectado2 = df_proyectado
df_proyectado2.head(10)


# #### 3.4.1-2 CREACIÓN NUEVO DATAFRAME DE COPIA 2.

# In[101]:


df_proyectado2_1M = df_proyectado_1M
df_proyectado2_1M.head(10)


# #### 3.4.2 LIMPIEZA DE DATAFRAME Y SELECCIÓN DE COLUMNAS UTILES

# In[102]:


df_proyectado2 = df_proyectado2.drop(range(0, 6))
new_header = df_proyectado2.iloc[0]
df_proyectado2 = df_proyectado2[1:]
df_proyectado2.columns = new_header
df_proyectado2 = df_proyectado2.loc[:, ["PROYECTO", "PROYECTO2", "INGRESO","MATERIALES","MANO DE OBRA"]]
df_proyectado2.sample(10)


# #### 3.4.2-2 LIMPIEZA DE DATAFRAME Y SELECCIÓN DE COLUMNAS UTILES 2

# In[103]:


df_proyectado2_1M = df_proyectado2_1M.drop(range(0, 6))
new_header = df_proyectado2_1M.iloc[0]
df_proyectado2_1M = df_proyectado2_1M[1:]
df_proyectado2_1M.columns = new_header
df_proyectado2_1M = df_proyectado2_1M.loc[:, ["PROYECTO", "PROYECTO2", "INGRESO","MATERIALES","MANO DE OBRA"]]
df_proyectado2_1M.sample(10)


# In[104]:


# INSPECCIÓN VISUAL 1
df_proyectado2_1M[df_proyectado2_1M["PROYECTO"]=="P-1726"]


# #### 3.4.3 TRATAMIENTO DE DATOS NAN

# In[105]:


# seleccionar las columnas deseadas
df_proyectado3 = df_proyectado2[["PROYECTO", "PROYECTO2", "INGRESO","MATERIALES","MANO DE OBRA"]]
# eliminar la columna índice
df_proyectado3 = df_proyectado3.reset_index(drop=True)
# eliminar las filas que contengan NaN en la columna P
df_proyectado3 = df_proyectado3.dropna(subset=['PROYECTO'])
# reemplazar los valores NaN en la columna INGRESO por cero
df_proyectado3['INGRESO'] = df_proyectado3['INGRESO'].fillna(0)
df_proyectado3['MATERIALES'] = df_proyectado3['MATERIALES'].fillna(0)
df_proyectado3['MANO DE OBRA'] = df_proyectado3['MANO DE OBRA'].fillna(0)

# renombrar la columna P a CODIGO_PROYECTO
df_proyectado3 = df_proyectado3.rename(columns={'PROYECTO': 'CODIGO_PROYECTO'})
df_proyectado3 = df_proyectado3.rename(columns={'PROYECTO2': 'PROYECTO'})

# poner en mayúscula el contenido de las columnas CODIGO_PROYECTO y PROYECTO
df_proyectado3['CODIGO_PROYECTO'] = df_proyectado3['CODIGO_PROYECTO'].str.upper()
df_proyectado3['PROYECTO'] = df_proyectado3['PROYECTO'].str.upper()

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_proyectado3  : ", df_proyectado3.shape)

df_proyectado3.sample(10)


# In[106]:


print(df_proyectado3.columns)


# In[107]:


# Eliminar la columna '6'
df_proyectado3 = df_proyectado3.rename_axis(None, axis=1)
df_proyectado3 = df_proyectado3.dropna(subset=['CODIGO_PROYECTO'])

print(df_proyectado3.shape)
df_proyectado3.sample(15)


# #### 3.4.3-2 TRATAMIENTO DE DATOS NAN 2

# In[108]:


# seleccionar las columnas deseadas
df_proyectado3_1M = df_proyectado2_1M[["PROYECTO", "PROYECTO2", "INGRESO","MATERIALES","MANO DE OBRA"]]
# eliminar la columna índice
df_proyectado3_1M = df_proyectado3_1M.reset_index(drop=True)
# eliminar las filas que contengan NaN en la columna P
df_proyectado3_1M = df_proyectado3_1M.dropna(subset=['PROYECTO'])
# reemplazar los valores NaN en la columna INGRESO por cero
df_proyectado3_1M['INGRESO'] = df_proyectado3_1M['INGRESO'].fillna(0)
df_proyectado3_1M['MATERIALES'] = df_proyectado3_1M['MATERIALES'].fillna(0)
df_proyectado3_1M['MANO DE OBRA'] = df_proyectado3_1M['MANO DE OBRA'].fillna(0)

# renombrar la columna P a CODIGO_PROYECTO
df_proyectado3_1M = df_proyectado3_1M.rename(columns={'PROYECTO': 'CODIGO_PROYECTO'})
df_proyectado3_1M = df_proyectado3_1M.rename(columns={'PROYECTO2': 'PROYECTO'})

# poner en mayúscula el contenido de las columnas CODIGO_PROYECTO y PROYECTO
df_proyectado3_1M['CODIGO_PROYECTO'] = df_proyectado3_1M['CODIGO_PROYECTO'].str.upper()
df_proyectado3_1M['PROYECTO'] = df_proyectado3_1M['PROYECTO'].str.upper()

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_proyectado3_1M  : ", df_proyectado3_1M.shape)

df_proyectado3_1M.sample(10)


# In[109]:


# INSPECCIÓN VISUAL 1
df_proyectado3_1M[df_proyectado3_1M["CODIGO_PROYECTO"]=="P-1726"]


# #### 3.4.4 SE AGREGA LA COLUMNA TOTAL PARA EL DATAFRAME Y SE FILTRA POR EL MES EN CURSO

# In[110]:


# Obtener el año y mes actual

import datetime

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month

# Calcula la sumatoria de la columna 'INGRESO'
total_ingreso = df_proyectado3['INGRESO'].sum()
total_materiales = df_proyectado3['MATERIALES'].sum()
total_mano_obra = df_proyectado3['MANO DE OBRA'].sum()

# Crea la fila 'TOTAL'
total_row = {'CODIGO_PROYECTO': 'TOTAL', 'PROYECTO': '', 'INGRESO': total_ingreso,'MATERIALES': total_materiales,'MANO DE OBRA': total_mano_obra}

# Crea un DataFrame con la fila 'TOTAL'
df_total = pd.DataFrame([total_row])

# Concatena el DataFrame original con el DataFrame que contiene la fila 'TOTAL'
df_proyectado3 = pd.concat([df_proyectado3, df_total], ignore_index=True)

#Agreación de columnas para estandarización
df_proyectado3["TOTAL"] = df_proyectado3["INGRESO"]
df_proyectado3["TIPO_CUENTA"] = "INGRESO"
df_proyectado3["MES"] = current_month 
df_proyectado3["AÑO"] = current_year 
df_proyectado3["ORIGEN"] = "PROYECTADO" 

# Se reemplazan valores NaN en 0 
df_proyectado3 = df_proyectado3.fillna(value=0)

# Multiplicar las columnas MATERIALES y MANO DE OBRA por -1 para obtener valores negativos
df_proyectado3[['MATERIALES', 'MANO DE OBRA']] = df_proyectado3[['MATERIALES', 'MANO DE OBRA']].mul(-1)

# Se calcula la columna TOTAL como la suma de INGRESO, MATERIALES y MANO DE OBRA
df_proyectado3['TOTAL'] = df_proyectado3[['INGRESO', 'MATERIALES', 'MANO DE OBRA']].sum(axis=1)

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_proyectado3  : ", df_proyectado3.shape)
df_proyectado3.sample(5)


# In[111]:


df_proyectado3['INGRESO'].sum()


# #### 3.4.4-2 SE AGREGA LA COLUMNA TOTAL PARA EL DATAFRAME Y SE FILTRA POR EL MES EN CURSO 2

# In[112]:


# Obtener el año y mes actual

import datetime

current_year = datetime.datetime.now().year
last_month = (fecha_actual - timedelta(days=30)).month

# Calcula la sumatoria de la columna 'INGRESO'
total_ingreso    = df_proyectado3_1M['INGRESO'].sum()
total_materiales = df_proyectado3_1M['MATERIALES'].sum()
total_mano_obra  = df_proyectado3_1M['MANO DE OBRA'].sum()

# Crea la fila 'TOTAL'
total_row = {'CODIGO_PROYECTO': 'TOTAL', 'PROYECTO': '', 'INGRESO': total_ingreso,'MATERIALES': total_materiales,'MANO DE OBRA': total_mano_obra}

# Crea un DataFrame con la fila 'TOTAL'
df_total = pd.DataFrame([total_row])

# Concatena el DataFrame original con el DataFrame que contiene la fila 'TOTAL'
df_proyectado3_1M = pd.concat([df_proyectado3_1M, df_total], ignore_index=True)

#Agreación de columnas para estandarización
df_proyectado3_1M["TOTAL"] = df_proyectado3["INGRESO"]
df_proyectado3_1M["TIPO_CUENTA"] = "INGRESO"
df_proyectado3_1M["MES"] = last_month 
df_proyectado3_1M["AÑO"] = current_year 
df_proyectado3_1M["ORIGEN"] = "PROYECTADO" 

# Se reemplazan valores NaN en 0 
df_proyectado3_1M = df_proyectado3_1M.fillna(value=0)

# Multiplicar las columnas MATERIALES y MANO DE OBRA por -1 para obtener valores negativos
df_proyectado3_1M[['MATERIALES', 'MANO DE OBRA']] = df_proyectado3_1M[['MATERIALES', 'MANO DE OBRA']].mul(-1)

# Se calcula la columna TOTAL como la suma de INGRESO, MATERIALES y MANO DE OBRA
df_proyectado3_1M['TOTAL'] = df_proyectado3_1M[['INGRESO', 'MATERIALES', 'MANO DE OBRA']].sum(axis=1)

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_proyectado3_1M  : ", df_proyectado3_1M.shape)
df_proyectado3_1M.sample(5)


# In[113]:


# INSPECCIÓN VISUAL 1
df_proyectado3_1M[df_proyectado3_1M["CODIGO_PROYECTO"]=="P-1726"]


# #### 3.4.5 ESTRATEGIA PARA TRANSFORMAR LAS COLUMNAS DE MANO DE OBRA, MATERIALES E INGRESOS EN FILAS. 

# In[114]:


print("Dimensiones solo df_proyectado3 antes de cambios",df_proyectado3.shape)

# Crear el subDataFrame sin las columnas MANO DE OBRA, MATERIALES, TOTAL y TIPO_CUENTA
df_sub = df_proyectado3.drop(['MANO DE OBRA', 'MATERIALES', 'TOTAL', 'TIPO_CUENTA'], axis=1)

# Agregar la columna TIPO_CUENTA con el valor INGRESO
df_sub['TIPO_CUENTA'] = 'INGRESO'

# Renombrar la columna INGRESO como TOTAL
df_sub = df_sub.rename(columns={'INGRESO': 'TOTAL'})
print("Dimensiones solo INGRESO",df_sub.shape)

# Crear el subDataFrame sin las columnas INGRESO, MATERIALES, TOTAL y TIPO_CUENTA
df_sub2 = df_proyectado3.drop(['INGRESO', 'MATERIALES', 'TOTAL', 'TIPO_CUENTA'], axis=1)

# Agregar la columna TIPO_CUENTA con el valor MANO DE OBRA
df_sub2['TIPO_CUENTA'] = 'MANO DE OBRA'

# Renombrar la columna MANO DE OBRA como TOTAL
df_sub2 = df_sub2.rename(columns={'MANO DE OBRA': 'TOTAL'})
print("Dimensiones solo MANO DE OBRA",df_sub2.shape)


# Crear el subDataFrame sin las columnas INGRESO, MANO DE OBRA, TOTAL y TIPO_CUENTA
df_sub3 = df_proyectado3.drop(['INGRESO', 'MANO DE OBRA', 'TOTAL', 'TIPO_CUENTA'], axis=1)

# Agregar la columna TIPO_CUENTA con el valor MANO DE OBRA
df_sub3['TIPO_CUENTA'] = 'MATERIALES'

# Renombrar la columna MANO DE OBRA como TOTAL
df_sub3 = df_sub3.rename(columns={'MATERIALES': 'TOTAL'})
print("Dimensiones solo MATERIALES",df_sub3.shape)

# Concatenar los DataFrames verticalmente
df_proyectado4 = pd.concat([df_sub, df_sub2, df_sub3])

# Mostrar el nuevo DataFrame concatenado

print("Dimensiones solo df_proyectado4 después de cambios",df_proyectado4.shape)

df_proyectado4.sample(10)


# #### 3.4.5-2 ESTRATEGIA PARA TRANSFORMAR LAS COLUMNAS DE MANO DE OBRA, MATERIALES E INGRESOS EN FILAS 2  

# In[115]:


print("Dimensiones solo df_proyectado3 antes de cambios",df_proyectado3_1M.shape)

# Crear el subDataFrame sin las columnas MANO DE OBRA, MATERIALES, TOTAL y TIPO_CUENTA
df_sub = df_proyectado3_1M.drop(['MANO DE OBRA', 'MATERIALES', 'TOTAL', 'TIPO_CUENTA'], axis=1)

# Agregar la columna TIPO_CUENTA con el valor INGRESO
df_sub['TIPO_CUENTA'] = 'INGRESO'

# Renombrar la columna INGRESO como TOTAL
df_sub = df_sub.rename(columns={'INGRESO': 'TOTAL'})
print("Dimensiones solo INGRESO",df_sub.shape)

# Crear el subDataFrame sin las columnas INGRESO, MATERIALES, TOTAL y TIPO_CUENTA
df_sub2 = df_proyectado3_1M.drop(['INGRESO', 'MATERIALES', 'TOTAL', 'TIPO_CUENTA'], axis=1)

# Agregar la columna TIPO_CUENTA con el valor MANO DE OBRA
df_sub2['TIPO_CUENTA'] = 'MANO DE OBRA'

# Renombrar la columna MANO DE OBRA como TOTAL
df_sub2 = df_sub2.rename(columns={'MANO DE OBRA': 'TOTAL'})
print("Dimensiones solo MANO DE OBRA",df_sub2.shape)


# Crear el subDataFrame sin las columnas INGRESO, MANO DE OBRA, TOTAL y TIPO_CUENTA
df_sub3 = df_proyectado3_1M.drop(['INGRESO', 'MANO DE OBRA', 'TOTAL', 'TIPO_CUENTA'], axis=1)

# Agregar la columna TIPO_CUENTA con el valor MANO DE OBRA
df_sub3['TIPO_CUENTA'] = 'MATERIALES'

# Renombrar la columna MANO DE OBRA como TOTAL
df_sub3 = df_sub3.rename(columns={'MATERIALES': 'TOTAL'})
print("Dimensiones solo MATERIALES",df_sub3.shape)

# Concatenar los DataFrames verticalmente
df_proyectado4_1M = pd.concat([df_sub, df_sub2, df_sub3])

# Mostrar el nuevo DataFrame concatenado

print("Dimensiones solo df_proyectado4 después de cambios",df_proyectado4_1M.shape)

df_proyectado4_1M.sample(10)


# In[116]:


# INSPECCIÓN VISUAL 1
df_proyectado4_1M[df_proyectado4_1M["CODIGO_PROYECTO"]=="P-1726"]


# #### 3.4.6 CAMBIO DE VALORES EN COLUMNA TIPO_CUENTA

# In[117]:


# Cambiar los valores de la columna TIPO_CUENTA
df_proyectado4['TIPO_CUENTA'] = df_proyectado4['TIPO_CUENTA'].replace({'MATERIALES': '2. COSTO MATERIALES', 'MANO DE OBRA': '3. COSTO MANO DE OBRA', 'INGRESO': '1. INGRESO'})

# Mostrar el DataFrame con los valores cambiados
print("Dimensiones solo df_proyectado4 después de cambios",df_proyectado4.shape)
df_proyectado4.sample(10)


# In[118]:


# TEST TOTAL "INGRESO" 

df_proyectado4_test = df_proyectado4[df_proyectado4['TIPO_CUENTA'] == '1. INGRESO']
df_proyectado4_test                                     


# #### 3.4.6-2 CAMBIO DE VALORES EN COLUMNA TIPO_CUENTA 2

# In[119]:


# Cambiar los valores de la columna TIPO_CUENTA
df_proyectado4_1M['TIPO_CUENTA'] = df_proyectado4_1M['TIPO_CUENTA'].replace({'MATERIALES': '2. COSTO MATERIALES', 'MANO DE OBRA': '3. COSTO MANO DE OBRA', 'INGRESO': '1. INGRESO'})

# Mostrar el DataFrame con los valores cambiados
print("Dimensiones solo df_proyectado4 después de cambios",df_proyectado4_1M.shape)
df_proyectado4_1M.sample(10)


# In[120]:


df_proyectado4_1M[df_proyectado4_1M["CODIGO_PROYECTO"]=="P-1726"]


# In[121]:


df_proyectado4.to_csv('archivos_respaldo/df_proyectado4.csv', mode='a')
df_proyectado4_1M.to_csv('archivos_respaldo/df_proyectado4_1M.csv', mode='a')


# ### 3.5 TRATAMIENTO LIBRO MAYOR AÑOS ANTERIORES

# #### 3.5.1 - REVISIÓN DE LOS DATOS

# In[122]:


df_libro_mayor_old.shape


# In[123]:


df_libro_mayor_old.describe()


# #### 3.5.2 - Estandarización campo "Debito" y Crédito

# In[124]:


# Se crean nuevos campos para trabajar "Debito" y "Credito".

df_libro_mayor_old['Debito_2'] = pd.to_numeric(df_libro_mayor_old['Debito'], errors='coerce')
df_libro_mayor_old['Credito_2'] = pd.to_numeric(df_libro_mayor_old['Credito'], errors='coerce')

# Se reemplaza el valor de los NoNe y Nan 

df_libro_mayor_old['Credito_2'] = df_libro_mayor_old['Credito_2'].fillna(0)

df_libro_mayor_old.head(5)


# #### 3.5.3 - Creación campo Codigo_proyecto

# In[125]:


# Se crean una nueva columna para manejar el código del proyecto 

df_libro_mayor_old['CODIGO_PROYECTO'] = df_libro_mayor_old['Primer_Analisis']

cols = df_libro_mayor_old.columns.tolist() # Obtiene el nombre de todas las columnas en una lista
cols.insert(0, cols.pop(cols.index('CODIGO_PROYECTO'))) # Extrae la columna 'Codigo_proyecto', la inserta en la posición 0 y actualiza la lista
df_libro_mayor_old = df_libro_mayor_old.reindex(columns=cols) # Reindexa el dataframe con las columnas en el orden actualizado

# Transformación a mayúscula código del proyecto
df_libro_mayor_old['CODIGO_PROYECTO'] = df_libro_mayor_old['CODIGO_PROYECTO'].str.upper()

df_libro_mayor_old.head(5)


# #### 3.5.4 - Creación de campo total

# In[126]:


df_libro_mayor_old['TOTAL'] = df_libro_mayor_old['Credito_2'] - df_libro_mayor_old['Debito_2']
df_libro_mayor_old.head(5)


# #### 3.5.5 - Creación campo tipo_cuenta "basado en el campo cta_Contable"

# In[127]:


# Función para categorizar la columna 'Cta_Contable'
def categorizar_cta_contable(cta_contable):
    if cta_contable =="3101030-000" or cta_contable == "3401002-000":
        return '1. INGRESO'
    elif cta_contable == "4101010-000":
        return '2. COSTO MATERIALES'
    elif cta_contable == "4150002-000":
        return '3. COSTO MANO DE OBRA'
    elif cta_contable == "4150002-002":
        return '4. COSTO SUPERVISIÓN'
    else:
        return 'OTRA'

# Crear la nueva columna 'Tipo_cuenta' aplicando la función
df_libro_mayor_old['Tipo_cuenta'] = df_libro_mayor_old['Cta_Contable'].apply(categorizar_cta_contable)
df_libro_mayor_old.sample(5)


# In[128]:


df_libro_mayor_old['Tipo_cuenta'].unique()


# In[129]:


# Revisión de los datos creados

df_libro_mayor_old_piv = pd.pivot_table(df_libro_mayor_old, values=['Debito_2','Credito_2','TOTAL'], index=['Tipo_cuenta','Año','Mes'], aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')
df_libro_mayor_old_piv = pd.DataFrame(df_libro_mayor_old_piv.to_records())

#df_libro_mayor_piv.head(5)
df_libro_mayor_old_piv.sample(10)


# In[ ]:





# #### 3.5.6 - Se eliminan números de proyectos que no deben ser parte del análisis

# In[130]:


# Se crea una copia del dataframe original debido que se reduciran las dimensiones
df_libro_mayor_old2 = df_libro_mayor_old.copy()

# Se identifican los códigos de proyecto disponibles
print("Proyectos disponibles antes de la reducción : ")
print(df_libro_mayor_old2["CODIGO_PROYECTO"].unique())
print("=======================================================================")
print("Dimensiones del dataframe antes de la reducción : ")
print(df_libro_mayor_old2.shape)


# ##### 3.5.6.1 - Se crea un subdataframe para COSTOS SUPERVISIÓN (separando lo que tiene P-OFICINA y cta_contable 4150002-002)

# In[131]:


# Se crea un dataframe separado para tratar los que poseen proyecto "P-OFICINA" ya que los costos de supervisión solo aplican al total
df_libro_mayor_old2_2 = df_libro_mayor_old2.copy()

# Filtrar el DataFrame
df_libro_mayor_old2_2 = df_libro_mayor_old2_2[(df_libro_mayor_old2_2['CODIGO_PROYECTO'] == 'P-OFICINA') & (df_libro_mayor_old2_2['Cta_Contable'] == '4150002-002')]

# Mostrar el DataFrame filtrado
df_libro_mayor_old2_2


# In[132]:


# Elimina los registros NaN en la columna Codigo_proyecto
df_libro_mayor_old2 = df_libro_mayor_old2.dropna(subset=['CODIGO_PROYECTO'])

# Define una lista de valores a eliminar
valores_a_eliminar = ['P-PROYECTOS', 'P-SERVICIOS','P-OFICINA', 'P-ANALISIS PROYE', '13056802-5', '16411600-K', '18800250-1','P-MANTENCIÓN','18800250','13056802','16411600']

# Crea una máscara booleana que identifica las filas que contienen los valores a eliminar
mask = df_libro_mayor_old2['CODIGO_PROYECTO'].isin(valores_a_eliminar)

# Crea un nuevo dataframe sin las filas que contienen los valores a eliminar
df_libro_mayor_old2 = df_libro_mayor_old2[~mask]


# In[133]:


# Se identifican los códigos de proyecto disponibles
print("Proyectos disponibles antes de la reducción : ")
print(df_libro_mayor_old.shape)
print(df_libro_mayor_old["CODIGO_PROYECTO"].unique())
print("=======================================================================")
print("Dimensiones del dataframe antes de la reducción : ")
print(df_libro_mayor_old2.shape)
print(df_libro_mayor_old2["CODIGO_PROYECTO"].unique())


# #### 3.5.7 - Se crea un nuevo campo de fecha basado en la fecha original

# In[134]:


df_libro_mayor_old2['Fecha2'] = pd.to_datetime(df_libro_mayor_old2['Año'].astype(str) + '-' + df_libro_mayor_old2['Mes'].astype(str) + '-1')
df_libro_mayor_old2.sample(5)


# ##### 3.5.7.1 - Se crea un nuevo campo de fecha basado en la fecha original para  COSTOS SUPERVISIÓN

# In[135]:


df_libro_mayor_old2_2['Fecha2'] = pd.to_datetime(df_libro_mayor_old2_2['Año'].astype(str) + '-' + df_libro_mayor_old2_2['Mes'].astype(str) + '-1')
df_libro_mayor_old2_2.sample(5)


# In[136]:


df_libro_mayor_old2_2['Tipo_cuenta'].unique()


# In[137]:


df_libro_mayor_old2_2[df_libro_mayor_old2_2["Primer_Analisis"] == "P-1673"]


# #### 3.5.8 - Se realiza pivote final del dataframe

# In[138]:


# Se exploran las columnas:
df_libro_mayor_old2.columns


# In[139]:


# crear pivot table sin margenes

df_libro_mayor_old2_piv = pd.pivot_table(df_libro_mayor_old2, values=['Debito_2','Credito_2','TOTAL'], index=['CODIGO_PROYECTO','Tipo_cuenta','Fecha2','Año','Mes'], aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')
df_libro_mayor_old2_piv = pd.DataFrame(df_libro_mayor_old2_piv.to_records())

df_libro_mayor_old2_piv.sample(5)


# In[140]:


df_libro_mayor_old2_piv[df_libro_mayor_old2_piv["CODIGO_PROYECTO"] == "P-1704"]


# In[141]:


# Estas son las dimensiones del dataframe pivoteado:
df_libro_mayor_old2_piv.shape


# ##### 3.5.8.1 - Se realiza pivote final del dataframe paera COSTO SUPERVISIÓN

# In[142]:


# crear pivot table sin margenes

df_libro_mayor_old2_2_piv = pd.pivot_table(df_libro_mayor_old2_2, values=['Debito_2','Credito_2','TOTAL'], index=['CODIGO_PROYECTO','Tipo_cuenta','Fecha2','Año','Mes'], aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')
df_libro_mayor_old2_2_piv = pd.DataFrame(df_libro_mayor_old2_2_piv.to_records())

df_libro_mayor_old2_2_piv = df_libro_mayor_old2_2_piv[df_libro_mayor_old2_2_piv['CODIGO_PROYECTO'] != 'TOTAL']

# Se reemplaza el valor P-OFICINA por el valor TOTAL con lo cual se utilizará para unirlo al dataframe que crea las filas para el cálculo de los totales
df_libro_mayor_old2_2_piv['CODIGO_PROYECTO'] = df_libro_mayor_old2_2_piv['CODIGO_PROYECTO'].replace('P-OFICINA', 'TOTAL')

df_libro_mayor_old2_2_piv.sample()


# #### 3.5.9 - Se crea subdataframe para proyecto que considera el total con nombre "TOTAL", que se detalla por tipo_cuenta
# 

# In[143]:


df_libro_mayor_old2_piv2 = pd.pivot_table(df_libro_mayor_old2_piv, values=['Debito_2','Credito_2','TOTAL'], index=['Tipo_cuenta','Fecha2','Año','Mes'], aggfunc='sum', fill_value=0)
df_libro_mayor_old2_piv2 = pd.DataFrame(df_libro_mayor_old2_piv2.to_records())

# Agregamos la columna Codigo_proyecto con valor "TOTAL" en la primera columna
df_libro_mayor_old2_piv2.insert(loc=0, column='CODIGO_PROYECTO', value='TOTAL')

# Eliminamos los registros con Tipo_cuenta igual a "TOTAL"
df_libro_mayor_old2_piv2 = df_libro_mayor_old2_piv2[df_libro_mayor_old2_piv2['Tipo_cuenta'] != 'TOTAL']
df_libro_mayor_old2_piv2 = df_libro_mayor_old2_piv2[df_libro_mayor_old2_piv2['Tipo_cuenta'] != '']

df_libro_mayor_old2_piv2.sample(5)


# ##### 3.5.9.1 - Se anexa el dataframe creado con los totales con el dataframe creado a partir del punto 3.1.6.1 que contiene los costos de supervisión

# In[144]:


df_libro_mayor_old2_piv_fin = pd.concat([df_libro_mayor_old2_piv2, df_libro_mayor_old2_2_piv], ignore_index=True)
df_libro_mayor_old2_piv_fin.sample(10)


# #### 3.5.10 - Se concatenan los 2 dataframes resultantes

# In[145]:


print("=======================================================================")
print("Dimensiones del dataframe antes de la concatenación : ")
print(df_libro_mayor_old2_piv_fin.shape)


# In[146]:


df_libro_mayor_old3 = pd.concat([df_libro_mayor_old2_piv, df_libro_mayor_old2_piv_fin])
df_libro_mayor_old3.sort_values(by=['CODIGO_PROYECTO']).sample(5)
print(df_libro_mayor_old3.shape)


# #### 3.5.11 - Estandarización de campos 

# In[147]:


# Se estandarizan los campos con sus nombres y formatos, para un mayor entendimiento.

df_libro_mayor_old3 = df_libro_mayor_old3.rename(columns={
    'Codigo_proyecto': 'CODIGO_PROYECTO',
    'Tipo_cuenta': 'TIPO_CUENTA',
    'Fecha2': 'FECHA',
    'Año': 'AÑO',
    'Mes': 'MES',
    'Credito_2': 'CREDITO',
    'Debito_2': 'DEBITO'
})

df_libro_mayor_old3['AÑO'] = pd.to_numeric(df_libro_mayor_old3['AÑO'], downcast='integer')
df_libro_mayor_old3['MES'] = pd.to_numeric(df_libro_mayor_old3['MES'], downcast='integer')

df_libro_mayor_old3.sample(10)


# #### 3.5.14 Creación de columna MARGEN

# In[148]:


df_libro_mayor_old3_2 = df_libro_mayor_old3.copy()

#df_libro_mayor4_2['TOTAL'] = pd.to_numeric(df_libro_mayor4_2['AÑO'], downcast='float')

df_margen = df_libro_mayor_old3_2.groupby(['CODIGO_PROYECTO', 'MES']).apply(lambda x: pd.Series({
    'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['INGRESO','COSTO SUPERVISIÓN', 'COSTO MANO DE OBRA', 'COSTO MATERIALES']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == 'INGRESO', 'TOTAL'].sum()
}))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


# In[149]:


print("=======================================================================")
print("Dimensiones del dataframe antes del merge : ")
print(df_libro_mayor_old3.shape)
print("=======================================================================")
print("Dimensiones del dataframe antes del merge : ")
print(df_margen.shape)


# In[150]:


df_libro_mayor_old3 = pd.merge(df_libro_mayor_old3, df_margen, on=['CODIGO_PROYECTO', 'MES'], how='left')
#EJEMPLO
#df_libro_mayor5[df_libro_mayor5["CODIGO_PROYECTO"]=="P-1706"]
df_libro_mayor_old3[df_libro_mayor_old3["CODIGO_PROYECTO"]=="TOTAL"]

# Se estandariza el valor TOTAL a 1.TOTAL para que pueda ser seleccionado desde los filtros del Dashboard.
df_libro_mayor_old3['CODIGO_PROYECTO'] = df_libro_mayor_old3['CODIGO_PROYECTO'].apply(lambda x: '1. TOTAL' if x == 'TOTAL' else x)


# In[151]:


print("=======================================================================")
print("Dimensiones del dataframe después de la concatenación : ")
print(df_libro_mayor_old3.shape)


# In[152]:


df_libro_mayor_old3.sample(10)


# In[153]:


df_libro_mayor_old3.to_csv('archivos_respaldo/df_libro_mayor_old3.csv', mode='a')


# In[ ]:





# ### 3.6 TRATAMIENTO DE "PLANILLA PRESUPUESTO"

# In[154]:


# Se crea una copia del dataframe llamado "presupuesto"
df_presupuesto2 = df_presupuesto.copy()


# In[155]:


# Eliminar primera fila completa
df_presupuesto2 = df_presupuesto2.iloc[1:]

# Filtrar y mantener solo las columnas deseadas
df_presupuesto2 = df_presupuesto2[['PROYECTO', 'MONTO EN $']]

df_presupuesto2 = df_presupuesto2.rename(columns={'PROYECTO': 'CODIGO_PROYECTO', 'MONTO EN $': 'VALOR'})

df_presupuesto2.sample(10)


# In[156]:


# Se agregan nuevas columnas tipo de cuenta y Origen.

df_presupuesto2["TIPO_CUENTA"]= "1. INGRESO"
df_presupuesto2["ORIGEN"]= "PLANILLA PRESUPUESTO"

df_presupuesto2.sample(10)


# ### 3.7 TRATAMIENTO DE "TABLA PRESUPUESTO"

# In[157]:


# Se crea una copia del dataframe para realizar el tratamiento.

df_tabla_presupuesto2 = df_tabla_prespuesto.copy()
print("DIMENSIONES DATAFRAME df_tabla_prespuesto2", df_tabla_presupuesto2.shape)
df_tabla_presupuesto2.sample(5)


# In[158]:


# Se estandarizan los tipos de campo y se reemplazan valores NaN

df_tabla_presupuesto2['COSTO_UNITARIO'] = pd.to_numeric(df_tabla_presupuesto2['COSTO_UNITARIO'], errors='coerce')
df_tabla_presupuesto2['COSTO_TOTAL'] = pd.to_numeric(df_tabla_presupuesto2['COSTO_TOTAL'], errors='coerce')

# Se reemplaza el valor de los NoNe y Nan 

df_tabla_presupuesto2['COSTO_UNITARIO'] = df_tabla_presupuesto2['COSTO_UNITARIO'].fillna(0)
df_tabla_presupuesto2['COSTO_TOTAL'] = df_tabla_presupuesto2['COSTO_TOTAL'].fillna(0)

print("DIMENSIONES DATAFRAME df_tabla_prespuesto2", df_tabla_presupuesto2.shape)
df_tabla_presupuesto2.head(5)


# In[159]:


#### Creación de campo tipo_costo basado en el valor del a columna "PRODUCTO"

def clasificar_tipo_costo(producto):
    if   producto.upper().startswith("MANO DE OBRA"):
        return "3. COSTO MANO DE OBRA"
    elif producto.upper().startswith("SUPER"):
        return "4. COSTO SUPERVISIÓN"
    else:
        return "2. COSTO MATERIALES"

df_tabla_presupuesto2['TIPO_COSTO'] = df_tabla_presupuesto2['PRODUCTO'].apply(clasificar_tipo_costo)

df_tabla_presupuesto2.head(5)


# In[160]:


# crear pivot table sin margenes

df_tabla_presupuesto3 = pd.pivot_table(df_tabla_presupuesto2, values=['COSTO_TOTAL'], index=['CODIGO_PROYECTO','TIPO_COSTO'], aggfunc='sum', fill_value=0)

df_tabla_presupuesto3 = pd.DataFrame(df_tabla_presupuesto3.to_records())
df_tabla_presupuesto3.sample(10)


# In[161]:


# Se crea columna VALOR y se considera el valor en negativo.
df_tabla_presupuesto3['TOTAL'] = df_tabla_presupuesto3['COSTO_TOTAL'].apply(lambda x: x * -1 if x != 0 else 0)

# Se crea la columna de ORIGEN del archivo
df_tabla_presupuesto3["ORIGEN"] = "TABLA_PRESUPUESTO"

print("DIMENSIÓN DE LA TABLA ES", df_tabla_presupuesto3.shape)
df_tabla_presupuesto3.sample(5)


# In[162]:


# INSPECCIÓN VISUAL
df_tabla_presupuesto_testing = pd.pivot_table(df_tabla_presupuesto3, values=['TOTAL'], index=['TIPO_COSTO'], aggfunc='sum', fill_value=0)
df_tabla_presupuesto_testing


# In[163]:


df_tabla_presupuesto3.to_csv('archivos_respaldo/df_tabla_presupuesto3.csv', mode='a')


# In[ ]:





# ## 4.- **MERGE Y TRATAMIENTO DE DATAFRAMES 

# ### 4.1 - **MERGE PARA -> CUADRO FINANCIERO PROYECTOS 
# Merge entre Dataframes: df_libro_mayor5 y df_cod_proyecto

# In[164]:


print("Dimensiones antes del merge:")
print(df_libro_mayor5.shape)

df_libro_mayor6 = pd.merge(df_libro_mayor5, df_cod_proyecto, on=['CODIGO_PROYECTO'], how='left')

print("Dimensiones después del merge:")
print(df_libro_mayor6.shape)


# In[165]:


# Reemplazar los valores NaN por "TOTAL" cuando el CODIGO_PROYECTO sea "TOTAL"

cols_to_replace = ['CODIGO_PROYECTO', 'NOMBRE_OBRA', 'NOMBRE_CLIENTE']
df_libro_mayor6[cols_to_replace] = df_libro_mayor6[cols_to_replace].replace('TOTAL', '1. TOTAL')

# Quizás el código anterior sea redundante.
mask = df_libro_mayor6['CODIGO_PROYECTO'] == '1. TOTAL'
df_libro_mayor6.loc[mask, ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

# Se elimina la columna MERGE la que es innecesaria tener hasta ahora
df_libro_mayor6 = df_libro_mayor6.drop('MARGEN', axis=1)

df_libro_mayor6[df_libro_mayor6["CODIGO_PROYECTO"]== "1. TOTAL"].head(5)


# #### 4.1.1 - AGREGACIÓN DE NUEVA COLUMNA DE TOTAL PARA AGREGAR EN GRÁFICO.
# Se agrega nueva columna de total pero considerando el valor de los tipos de costo con valores positivos.

# In[166]:


# Crear la nueva columna 'TOTAL_2' con los valores de 'TOTAL' positivos
df_libro_mayor6['TOTAL_2'] = np.where(df_libro_mayor6['TIPO_CUENTA'] != 'INGRESO', np.abs(df_libro_mayor6['TOTAL']), df_libro_mayor6['TOTAL'])
df_libro_mayor6.sample(10)


# #### 4.1.2 - AJUSTES DE COLUMNAS 

# In[167]:


# Renombrar los valores de la columna CODIGO_PROYECTO
df_libro_mayor6['TIPO_CUENTA'] = df_libro_mayor6['TIPO_CUENTA'].replace({
    'INGRESO': '1. INGRESO',
    'COSTO MATERIALES': '2. COSTO MATERIALES',
    'COSTO MANO DE OBRA': '3. COSTO MANO DE OBRA',
    'COSTO SUPERVISIÓN': '4. COSTO SUPERVISIÓN'
})

df_libro_mayor6['CODIGO_PROYECTO'] = df_libro_mayor6['CODIGO_PROYECTO'].replace({
    'TOTAL': '1. TOTAL'})


# In[168]:


# Ordenar el DataFrame por la columna CODIGO_PROYECTO
df_libro_mayor6 = df_libro_mayor6.sort_values('CODIGO_PROYECTO')

# Mover la fila con CODIGO_PROYECTO = '1. TOTAL' al primer lugar
df_libro_mayor6 = pd.concat([df_libro_mayor6[df_libro_mayor6['CODIGO_PROYECTO'] == '1. TOTAL'],
                            df_libro_mayor6[df_libro_mayor6['CODIGO_PROYECTO'] != '1. TOTAL']])

df_libro_mayor6['NOMBRE_OBRA'] = df_libro_mayor6['NOMBRE_OBRA'].str.upper()
df_libro_mayor6['NOMBRE_CLIENTE'] = df_libro_mayor6['NOMBRE_CLIENTE'].str.upper()

# Reiniciar los índices del DataFrame
df_libro_mayor6 = df_libro_mayor6.reset_index(drop=True)
df_libro_mayor6.sample(5)


# #### 4.1.3 - CREACIÓN DE COLUMNA MARGEN

# In[169]:


df_margen = df_libro_mayor6.groupby(['CODIGO_PROYECTO', 'MES']).apply(lambda x: pd.Series({
    'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA','4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
}))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)

#warnings.filterwarnings("ignore", category=FutureWarning, message="Inferring datetime64.*")

# mostrar el DataFrame resultante
df_margen.sample(10)

df_libro_mayor6 = pd.merge(df_libro_mayor6, df_margen, on=['CODIGO_PROYECTO', 'MES'], how='left')

# INSPECCIÓN VISUAL 1
df_libro_mayor6[df_libro_mayor6["CODIGO_PROYECTO"]=="P-1704"]


# In[170]:


df_libro_mayor6.to_csv('archivos_respaldo/df_libro_mayor6.csv', mode='a')


# In[ ]:





# ### 4.2 - **MERGE PARA -> YTD AÑO EN CURSO HASTA MES CERRADO
# MERGE ENTRE df_libro_mayor_ytd_closed_piv y df_cod_proyecto

# In[171]:


print("Dimensiones antes del merge:")
df_libro_mayor_ytd_closed_piv.shape


# In[172]:


df_ytd_cerrado = df_libro_mayor_ytd_closed_piv.copy()


# In[173]:


# Se realiza merge con Nombre de Obra y Cliente.

print("Dimensiones mes_en_curso antes de cambios: ", df_ytd_cerrado.shape)
df_ytd_cerrado = df_ytd_cerrado.merge(df_cod_proyecto, on='CODIGO_PROYECTO', how='left')
print("Dimensiones mes_en_curso2 antes de cambios: ", df_ytd_cerrado.shape)
df_ytd_cerrado.sample(10)


# In[174]:


# Se reemplazan nombres de TIPO_CUENTA

df_ytd_cerrado['TIPO_CUENTA'] = df_ytd_cerrado['TIPO_CUENTA'].replace({
    'INGRESO': '1. INGRESO',
    'COSTO MATERIALES': '2. COSTO MATERIALES',
    'COSTO MANO DE OBRA': '3. COSTO MANO DE OBRA',
    'COSTO SUPERVISIÓN': '4. COSTO SUPERVISIÓN'
})
df_ytd_cerrado.sample(10)


# In[175]:


# INSPECCIÓN VISUAL 1 
df_ytd_cerrado[df_ytd_cerrado["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[176]:


#Se renombra "TOTAL" a "1. TOTAL" para que se pueda visualizar en el dashboard.

cols_to_replace = ['CODIGO_PROYECTO', 'NOMBRE_OBRA', 'NOMBRE_CLIENTE']
df_ytd_cerrado[cols_to_replace] = df_ytd_cerrado[cols_to_replace].replace('TOTAL', '1. TOTAL')
mask = df_ytd_cerrado['CODIGO_PROYECTO'] == '1. TOTAL'
df_ytd_cerrado.loc[mask, ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'
df_ytd_cerrado.sample(4)


# In[177]:


# INSPECCIÓN VISUAL 1
df_ytd_cerrado[df_ytd_cerrado["CODIGO_PROYECTO"]=="1. TOTAL"]


# #### 4.2.1 - MERGE CON "df_libro_mayor5_base2" PARA CREAR DATAFRAME FINAL

# In[178]:


print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado   : ", df_ytd_cerrado.shape)

df_ytd_cerrado2 = df_ytd_cerrado.filter(["CODIGO_PROYECTO", "TIPO_CUENTA", "TOTAL"])

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado2 : ", df_ytd_cerrado2.shape)

df_ytd_cerrado2.sample(5)


# In[179]:


# Exploración dataframe base

df_libro_mayor5_base2.sample(5)


# In[180]:


# Merge Dataframe BASE 

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_base2   : ", df_libro_mayor5_base2.shape)

df_ytd_cerrado3 = df_libro_mayor5_base2.merge(df_ytd_cerrado2, on=['CODIGO_PROYECTO', 'TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado3       : ", df_ytd_cerrado3.shape)

df_ytd_cerrado3.sample(5)


# In[181]:


# INSPECCIÓN VISUAL 1

df_ytd_cerrado3[df_ytd_cerrado3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[182]:


# INSPECCIÓN VISUAL 2

df_ytd_cerrado3[df_ytd_cerrado3["CODIGO_PROYECTO"]=="P-1724"]


# #### 4.2.2 - SE REALIZA CREACIÓN DE COLUMNA MARGEN

# In[183]:


# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_ytd_cerrado3.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES','3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_margen       : ", df_margen.shape)

# mostrar el DataFrame resultante
df_margen.sample(10)


# In[184]:


df_margen[df_margen["CODIGO_PROYECTO"]=="P-1724"]


# In[185]:


# Merge Dataframe para agregar MARGEN

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado3   : ", df_ytd_cerrado3.shape)

df_ytd_cerrado3 = df_ytd_cerrado3.merge(df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado3 : ", df_ytd_cerrado3.shape)

df_ytd_cerrado3.sample(5)


# In[186]:


df_ytd_cerrado3.to_csv('archivos_respaldo/df_ytd_cerrado3.csv', index = False)


# ### 4.2-1 - MERGE PARA -> YTD AÑO EN CURSO HASTA MES CERRADO (PERSPECTIVA MES ANTERIOR)
# MERGE ENTRE df_libro_mayor_ytd_closed_2M y df_cod_proyecto

# In[187]:


print("Dimensiones antes del merge:")
df_libro_mayor_ytd_closed_2M.shape


# In[188]:


df_ytd_cerrado_2M = df_libro_mayor_ytd_closed_2M.copy()


# In[189]:


# Se realiza merge con Nombre de Obra y Cliente.

print("Dimensiones df_ytd_cerrado_2M antes de cambios: ", df_ytd_cerrado_2M.shape)
df_ytd_cerrado_2M = df_ytd_cerrado_2M.merge(df_cod_proyecto, on='CODIGO_PROYECTO', how='left')
print("Dimensiones df_ytd_cerrado_2M antes de cambios: ", df_ytd_cerrado_2M.shape)
df_ytd_cerrado_2M.sample(10)


# In[190]:


# Se reemplazan nombres de TIPO_CUENTA

df_ytd_cerrado_2M['TIPO_CUENTA'] = df_ytd_cerrado_2M['TIPO_CUENTA'].replace({
    'INGRESO': '1. INGRESO',
    'COSTO MATERIALES': '2. COSTO MATERIALES',
    'COSTO MANO DE OBRA': '3. COSTO MANO DE OBRA',
    'COSTO SUPERVISIÓN': '4. COSTO SUPERVISIÓN'
})
df_ytd_cerrado_2M.sample(10)


# In[191]:


# INSPECCIÓN VISUAL 1 
df_ytd_cerrado_2M[df_ytd_cerrado_2M["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[192]:


#Se renombra "TOTAL" a "1. TOTAL" para que se pueda visualizar en el dashboard.

cols_to_replace = ['CODIGO_PROYECTO', 'NOMBRE_OBRA', 'NOMBRE_CLIENTE']
df_ytd_cerrado_2M[cols_to_replace] = df_ytd_cerrado_2M[cols_to_replace].replace('TOTAL', '1. TOTAL')
mask = df_ytd_cerrado['CODIGO_PROYECTO'] == '1. TOTAL'
df_ytd_cerrado_2M.loc[mask, ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'
df_ytd_cerrado_2M.sample(4)


# In[193]:


# INSPECCIÓN VISUAL 1
df_ytd_cerrado_2M[df_ytd_cerrado_2M["CODIGO_PROYECTO"]=="1. TOTAL"]


# #### 4.2-1.1 - MERGE CON "df_libro_mayor5_base2" PARA CREAR DATAFRAME FINAL

# In[194]:


print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado_2M   : ", df_ytd_cerrado_2M.shape)

df_ytd_cerrado_2M_2 = df_ytd_cerrado_2M.filter(["CODIGO_PROYECTO", "TIPO_CUENTA", "TOTAL"])

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado_2M_2 : ", df_ytd_cerrado_2M_2.shape)

df_ytd_cerrado_2M_2.sample(5)


# In[195]:


df_margen[df_margen["CODIGO_PROYECTO"]=="P-1724"]


# In[196]:


# Exploración dataframe base

df_libro_mayor5_base2.sample(5)


# In[197]:


# Merge Dataframe BASE 

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_base2   : ", df_libro_mayor5_base2.shape)

df_ytd_cerrado_2M_3 = df_libro_mayor5_base2.merge(df_ytd_cerrado_2M_2, on=['CODIGO_PROYECTO', 'TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado_2M_3       : ", df_ytd_cerrado_2M_3.shape)

df_ytd_cerrado_2M_3.sample(5)


# In[198]:


# INSPECCIÓN VISUAL 1

df_ytd_cerrado_2M_3[df_ytd_cerrado_2M_3["CODIGO_PROYECTO"]=="1. TOTAL"]


# #### 4.2-1.2 - SE REALIZA CREACIÓN DE COLUMNA MARGEN

# In[199]:


# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_ytd_cerrado_2M_3.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES','3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_margen       : ", df_margen.shape)

# mostrar el DataFrame resultante
df_margen.sample(10)


# In[200]:


df_margen[df_margen["CODIGO_PROYECTO"]=="P-1724"]


# In[201]:


# Merge Dataframe para agregar MARGEN

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado_2M_3   : ", df_ytd_cerrado_2M_3.shape)

df_ytd_cerrado_2M_3 = df_ytd_cerrado_2M_3.merge(df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_ytd_cerrado_2M_3 : ", df_ytd_cerrado_2M_3.shape)

df_ytd_cerrado_2M_3.sample(5)


# In[202]:


df_ytd_cerrado_2M_3.to_csv('archivos_respaldo/df_ytd_cerrado_2M_3.csv', index = False)


# ### 4.3 - **MERGE PARA -> MES EN CURSO ENTRE LIBRO MAYOR + PROYECTADO 
# (DATAFRAMES: df_libro_mayor5_mec2 y df_proyectado4)

# #### 4.3.1 - CREACIÓN DE COPIA DE DATAFRAME "df_libro_mayor5_mec2" Y AJUSTES INICIALES

# In[203]:


# Ajuste del dataframe proveniente de LIBRO MAYOR

df_libro_mayor5_mec2.sample(5)
df_libro_mayor5_mec3 = df_libro_mayor5_mec2.drop(['CREDITO', 'DEBITO', 'MARGEN'], axis=1)
df_libro_mayor5_mec3.sample(5)


# In[204]:


# INSPECCIÓN VISUAL INICIAL 1

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_mec3  : ", df_libro_mayor5_mec3.shape)
df_libro_mayor5_mec3[df_libro_mayor5_mec3["CODIGO_PROYECTO"]=="P-1704"]


# In[205]:


# Se crea nueva columna que define el destino del uso del trozo del DATAFRAME proveniente del libro mayor

def determinar_origen(row):
    if row['TIPO_CUENTA'] in ['INGRESO', 'COSTO MATERIALES']:
        return 'REAL'
    elif row['TIPO_CUENTA'] in ['COSTO SUPERVISIÓN','COSTO MANO DE OBRA']:
        return 'REAL Y PROYECTADO'

df_libro_mayor5_mec3['DESTINO'] = df_libro_mayor5_mec3.apply(determinar_origen, axis=1)
print(df_libro_mayor5_mec3.shape)
df_libro_mayor5_mec3.sample(10)


# In[206]:


# Cambiar los valores de la columna TIPO_CUENTA
df_libro_mayor5_mec3['TIPO_CUENTA'] = df_libro_mayor5_mec3['TIPO_CUENTA'].replace({'COSTO MATERIALES': '2. COSTO MATERIALES', 'COSTO MANO DE OBRA': '3. COSTO MANO DE OBRA', 'INGRESO': '1. INGRESO','COSTO SUPERVISIÓN': '4. COSTO SUPERVISIÓN'})

print(df_libro_mayor5_mec3.shape)
df_libro_mayor5_mec3["TIPO_CUENTA"].unique()


# #### 4.3.2 - CREACIÓN DE COPIA DE DATAFRAME "df_proyectado4" Y AJUSTES INICIALES

# In[207]:


# Ajuste del dataframe proveniente de PROYECTADO

df_proyectado4.sample(5)
df_proyectado5 = df_proyectado4.drop(['PROYECTO'], axis=1)

# Se crea la columna Fecha
df_proyectado5['FECHA'] = pd.to_datetime(df_proyectado5['MES'].astype(str) + '-1-' + df_proyectado5['AÑO'].astype(str))

df_proyectado5.sample(5)


# In[208]:


# Se crea nueva columna que define el destino del uso del trozo del DATAFRAME proveniente del proyectado

def determinar_origen(row):
    if row['TIPO_CUENTA'] in ['1. INGRESO', '2. COSTO MATERIALES']:
        return 'PROYECTADO'

# Se realiza 
df_proyectado5['DESTINO'] = df_proyectado5.apply(determinar_origen, axis=1)
df_proyectado5 = df_proyectado5[df_proyectado5['TIPO_CUENTA'] != '3. COSTO MANO DE OBRA']


# Se reordenan las columnas para estandarizarlo como la que viene desde Libro Mayot
df_proyectado5 = df_proyectado5.reindex(columns=['CODIGO_PROYECTO', 'TIPO_CUENTA', 'FECHA', 'AÑO', 'MES', 'TOTAL', 'ORIGEN', 'DESTINO'])

df_proyectado5.sample(5)


# #### 4.3.3 - CONCATENACIÓN ENTRE DATAFRAMES DEL MES EN CURSO LIBRO MAYOR Y PROYECTADO

# In[209]:


# Se realiza concatenación entre ambos dataframes

print("Dimensiones df_libro_mayor5_mec3 antes de cambios: ", df_libro_mayor5_mec3.shape)
print("Dimensiones df_proyectado5 antes de cambios      : ", df_proyectado5.shape)

mes_en_curso = pd.concat([df_libro_mayor5_mec3, df_proyectado5])

print("Dimensiones dataframe final mes_en_curso después de concatenación  : ", mes_en_curso.shape)
mes_en_curso.sample(10)


# #### 4.3.4 - MERGE CON "df_cod_proyecto" PARA CREAR DATAFRAME FINAL

# In[210]:


print("Dimensiones mes_en_curso antes de cambios: ", mes_en_curso.shape)
mes_en_curso2 = mes_en_curso.merge(df_cod_proyecto, on='CODIGO_PROYECTO', how='left')
mes_en_curso2 = mes_en_curso2[['CODIGO_PROYECTO', 'NOMBRE_OBRA', 'NOMBRE_CLIENTE', 'TIPO_CUENTA', 'FECHA', 'AÑO', 'MES', 'TOTAL', 'ORIGEN', 'DESTINO']]
print("Dimensiones mes_en_curso2 antes de cambios: ", mes_en_curso2.shape)
mes_en_curso2.sample(10)


# In[211]:


#Para reemplazar los valores en blanco en las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" por el valor "TOTAL" cada vez que el valor de la columna "CODIGO_PROYECTO" es igual a "TOTAL", puedes hacer lo siguiente:

mes_en_curso2.loc[(mes_en_curso2['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso2['NOMBRE_OBRA'].isnull()), 'NOMBRE_OBRA'] = '1. TOTAL'
mes_en_curso2.loc[(mes_en_curso2['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso2['NOMBRE_CLIENTE'].isnull()), 'NOMBRE_CLIENTE'] = '1. TOTAL'
mes_en_curso2.sample(5)


# In[212]:


# INSPECCIÓN VISUAL 1

mes_en_curso2[mes_en_curso2["CODIGO_PROYECTO"]=="P-1704"]


# #### 4.3.5 - AGREGACIÓN DE TODOS TIPOS DE CUENTA

# In[213]:


print("Dimensiones Dataframe antes de cambios", mes_en_curso2.shape)

# definir nuevas filas
df_rows_to_add = []

for _, row in mes_en_curso2.iterrows():
    if row["TIPO_CUENTA"] == "1. INGRESO" and row["TOTAL"] == 0:
        row1 = row.copy()
        row1["TIPO_CUENTA"] = "1. INGRESO"
        row1["TOTAL"] = 0
        row1["ORIGEN"] = "AGREGACION"
        row1["DESTINO"] = "REAL"
        df_rows_to_add.append(row1)

        row2 = row.copy()
        row2["TIPO_CUENTA"] = "1. INGRESO"
        row2["TOTAL"] = 0
        row2["ORIGEN"] = "AGREGACION"
        row2["DESTINO"] = "PROYECTADO"
        df_rows_to_add.append(row2)

    elif row["TIPO_CUENTA"] == "2. COSTO MATERIALES" and row["TOTAL"] == 0:
        row1 = row.copy()
        row1["TIPO_CUENTA"] = "2. COSTO MATERIALES"
        row1["TOTAL"] = 0
        row1["ORIGEN"] = "AGREGACION"
        row1["DESTINO"] = "REAL"
        df_rows_to_add.append(row1)

        row2 = row.copy()
        row2["TIPO_CUENTA"] = "2. COSTO MATERIALES"
        row2["TOTAL"] = 0
        row2["ORIGEN"] = "AGREGACION"
        row2["DESTINO"] = "PROYECTADO"
        df_rows_to_add.append(row2)

    elif row["TIPO_CUENTA"] == "3. COSTO MANO DE OBRA" and row["TOTAL"] == 0:
        row1 = row.copy()
        row1["TIPO_CUENTA"] = "3. COSTO MANO DE OBRA"
        row1["TOTAL"] = 0
        row1["ORIGEN"] = "AGREGACION"
        row1["DESTINO"] = "REAL Y PROYECTADO"
        df_rows_to_add.append(row1)

  
    elif row["TIPO_CUENTA"] == "4. COSTO SUPERVISIÓN" and row["TOTAL"] == 0:
        row1 = row.copy()
        row1["TIPO_CUENTA"] = "4. COSTO SUPERVISIÓN"
        row1["TOTAL"] = 0
        row1["ORIGEN"] = "AGREGACION"
        row1["DESTINO"] = "REAL Y PROYECTADO"
        df_rows_to_add.append(row1)
        
        row2 = row.copy()
        row2["TIPO_CUENTA"] = "3. COSTO MANO DE OBRA"
        row2["TOTAL"] = 0
        row2["ORIGEN"] = "AGREGACION"
        row2["DESTINO"] = "REAL Y PROYECTADO"
        df_rows_to_add.append(row2)

# concatenar nuevas filas al DataFrame original
mes_en_curso2 = pd.concat([mes_en_curso2, pd.DataFrame(df_rows_to_add)], ignore_index=True)

# Se renombra "TOTAL" a "1. TOTAL" para que se pueda visualizar como primera opción en el dashboard.
mes_en_curso2['CODIGO_PROYECTO'] = mes_en_curso2['CODIGO_PROYECTO'].apply(lambda x: '1. TOTAL' if x == 'TOTAL' else x)

cols_to_replace = ['CODIGO_PROYECTO', 'NOMBRE_OBRA', 'NOMBRE_CLIENTE']
mes_en_curso2[cols_to_replace] = mes_en_curso2[cols_to_replace].replace('TOTAL', '1. TOTAL')
mask = mes_en_curso2['CODIGO_PROYECTO'] == '1. TOTAL'
mes_en_curso2.loc[mask, ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

# Cambiar los valores de la columna TIPO_CUENTA

print("Dimensiones Dataframe después de cambios", mes_en_curso2.shape)


# In[214]:


mes_en_curso2["TIPO_CUENTA"].unique()


# In[215]:


# INSPECCIÓN VISUAL 1
mes_en_curso2[mes_en_curso2["CODIGO_PROYECTO"]=="P-1644"]


# In[216]:


mes_en_curso2["TIPO_CUENTA"].unique()


# #### 4.3.6 - **CREACIÓN DATAFRAME PARA -> PROYECTADO

# In[217]:


# Se crea una copia del dataframe original mes_en_curso2

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso2       : ", mes_en_curso2.shape)

mes_en_curso2_1 = mes_en_curso2.copy()
mes_en_curso2_1 = mes_en_curso2[mes_en_curso2['DESTINO'].str.contains('PROYECTADO')]

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso2_1   : ", mes_en_curso2_1.shape)


print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso2_1     : ", mes_en_curso2_1.shape)

mes_en_curso_proy = pd.pivot_table(mes_en_curso2_1, values=['TOTAL'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum', fill_value=0)
mes_en_curso_proy = pd.DataFrame(mes_en_curso_proy.to_records())

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_proy  : ", mes_en_curso_proy.shape)

mes_en_curso_proy.sample(10)


# In[218]:


# TESTING VISUAL 1
mes_en_curso_proy[mes_en_curso_proy["CODIGO_PROYECTO"]=="P-1712"]


# In[219]:


# TESTING VISUAL 2
mes_en_curso_proy[mes_en_curso_proy["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.3.6.1 - MERGE CON DATAFRAME LIBRO MAYOR 2023 BASE 

# In[220]:


# Merge Dataframe BASE 

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_proy   : ", mes_en_curso_proy.shape)
print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_base2   : ", df_libro_mayor5_base2.shape)

mes_en_curso_proy2 = df_libro_mayor5_base2.merge(mes_en_curso_proy, on=['CODIGO_PROYECTO', 'TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_proy2       : ", mes_en_curso_proy2.shape)

mes_en_curso_proy2['TOTAL'] = mes_en_curso_proy2['TOTAL'].fillna(0)

mes_en_curso_proy2.sample(5)


# In[221]:


# TESTING VISUAL 1

mes_en_curso_proy2[mes_en_curso_proy2["CODIGO_PROYECTO"]=="P-1712"]


# In[222]:


# TESTING VISUAL 2
mes_en_curso_proy2[mes_en_curso_proy2["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.3.6.2 - SE RECALCULAN LOS TOTALES

# In[223]:


# Calcular la suma de los valores totales para cada tipo de cuenta

# Se eliminan totales excepto supervisión, para re hacer el calculo de totales

mes_en_curso_proy2 = mes_en_curso_proy2.drop(mes_en_curso_proy2[(mes_en_curso_proy2['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_proy2['TIPO_CUENTA'] != '4. COSTO SUPERVISIÓN')].index)

print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_proy2 : ", mes_en_curso_proy2.shape)

df_total = mes_en_curso_proy2.groupby('TIPO_CUENTA')['TOTAL'].sum().reset_index()
df_total['CODIGO_PROYECTO'] = '1. TOTAL'

# Agregar las filas adicionales al DataFrame
mes_en_curso_proy3 = pd.concat([mes_en_curso_proy2, df_total], ignore_index=True)

# Modificar las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" para "1. TOTAL"
mes_en_curso_proy3.loc[mes_en_curso_proy3['CODIGO_PROYECTO'] == '1. TOTAL', ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_proy3 : ", mes_en_curso_proy3.shape)

mes_en_curso_proy3.sample(10) 


# In[224]:


# TESTING VISUAL 2
mes_en_curso_proy3[mes_en_curso_proy3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[225]:


# SE ELIMINA COSTO SUPERVISIÓN DUPLICADO.

print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_proy3 : ", mes_en_curso_proy3.shape)

mes_en_curso_proy3 = mes_en_curso_proy3.drop(mes_en_curso_proy3[(mes_en_curso_proy3['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_proy3['TIPO_CUENTA'] == '4. COSTO SUPERVISIÓN') & (mes_en_curso_proy3['TOTAL_LB'].isnull())].index)

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_proy3 : ", mes_en_curso_proy3.shape)

mes_en_curso_proy3[mes_en_curso_proy3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[226]:


# TESTING VISUAL 1
mes_en_curso_proy3[mes_en_curso_proy3["CODIGO_PROYECTO"]=="P-1723"]


# In[227]:


# TESTING VISUAL 2
mes_en_curso_proy3[mes_en_curso_proy3["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.3.6.3 - CREACIÓN DE MARGEN

# In[228]:


#CREACIÓN DE MARGENES

mes_en_curso_proy4 = mes_en_curso_proy3.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = mes_en_curso_proy4.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


# In[229]:


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_proy4 : ", mes_en_curso_proy4.shape)

mes_en_curso_proy5 = pd.merge(mes_en_curso_proy4, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_proy5 : ", mes_en_curso_proy5.shape)
mes_en_curso_proy5.sample(10)


# In[230]:


# TESTING VISUAL 1
mes_en_curso_proy5[mes_en_curso_proy5["CODIGO_PROYECTO"]=="P-1723"]


# In[231]:


# TESTING VISUAL 2
mes_en_curso_proy5[mes_en_curso_proy5["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[232]:


# Respaldo de Dataframe mes en curso antes de abrirrlo
mes_en_curso_proy5.to_csv('archivos_respaldo/mes_en_curso_proy5.csv', mode='a')


# In[ ]:





# #### 4.3.7 - **CREACIÓN DATAFRAME PARA -> MES EN CURSO

# ##### 4.3.7.1 - TRATAMIENTO mes_en_curso2

# In[233]:


# Se crea una copia del dataframe original mes_en_curso2

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso2       : ", mes_en_curso2.shape)

mes_en_curso2_1 = mes_en_curso2.copy()
mes_en_curso2_1 = mes_en_curso2[mes_en_curso2['DESTINO'].str.contains('REAL')]

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso2_1   : ", mes_en_curso2_1.shape)


print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso2_1     : ", mes_en_curso2_1.shape)

mes_en_curso_real = pd.pivot_table(mes_en_curso2_1, values=['TOTAL'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum', fill_value=0)
mes_en_curso_real = pd.DataFrame(mes_en_curso_real.to_records())

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_real  : ", mes_en_curso_real.shape)

mes_en_curso_real.sample(10)


# In[234]:


# TESTING VISUAL 1

mes_en_curso_real[mes_en_curso_real["CODIGO_PROYECTO"]=="P-1712"]


# In[235]:


# TESTING VISUAL 2

mes_en_curso_real[mes_en_curso_real["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.3.7.2 - MERGE CON DATAFRAME LIBRO MAYOR 2023 BASE 

# In[236]:


# Merge Dataframe BASE 

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_real   : ", mes_en_curso_real.shape)
print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_base2   : ", df_libro_mayor5_base2.shape)

mes_en_curso_real2 = df_libro_mayor5_base2.merge(mes_en_curso_real, on=['CODIGO_PROYECTO', 'TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_real       : ", mes_en_curso_real.shape)

mes_en_curso_real2.sample(5)


# In[237]:


# TESTING VISUAL 1

mes_en_curso_real2[mes_en_curso_real2["CODIGO_PROYECTO"]=="P-1712"]


# In[238]:


# TESTING VISUAL 2

mes_en_curso_real2[mes_en_curso_real2["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.3.7.3 - SE RECALCULAN LOS TOTALES

# In[239]:


# Calcular la suma de los valores totales para cada tipo de cuenta

# Se eliminan totales excepto supervisión, para re hacer el calculo de totales

mes_en_curso_real2 = mes_en_curso_real2.drop(mes_en_curso_real2[(mes_en_curso_real2['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_real2['TIPO_CUENTA'] != '4. COSTO SUPERVISIÓN')].index)

print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_real2 : ", mes_en_curso_real2.shape)

df_total = mes_en_curso_real2.groupby('TIPO_CUENTA')['TOTAL'].sum().reset_index()
df_total['CODIGO_PROYECTO'] = '1. TOTAL'

# Agregar las filas adicionales al DataFrame
mes_en_curso_real3 = pd.concat([mes_en_curso_real2, df_total], ignore_index=True)

# Modificar las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" para "1. TOTAL"
mes_en_curso_real3.loc[mes_en_curso_real3['CODIGO_PROYECTO'] == '1. TOTAL', ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_real3 : ", mes_en_curso_real3.shape)

mes_en_curso_real3.sample(10)   


# In[240]:


# TESTING VISUAL 1

mes_en_curso_real3[mes_en_curso_real3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[241]:


# SE ELIMINA COSTO SUPERVISIÓN DUPLICADO.

print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_real3 : ", mes_en_curso_real3.shape)

mes_en_curso_real3 = mes_en_curso_real3.drop(mes_en_curso_real3[(mes_en_curso_real3['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_real3['TIPO_CUENTA'] == '4. COSTO SUPERVISIÓN') & (mes_en_curso_real3['TOTAL_LB'].isnull())].index)

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_real3 : ", mes_en_curso_real3.shape)

mes_en_curso_real3[mes_en_curso_real3["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.3.7.4 - CREACIÓN DE MARGEN

# In[242]:


#CREACIÓN DE MARGENES

mes_en_curso_real4 = mes_en_curso_real3.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = mes_en_curso_real4.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


# In[243]:


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_real4 : ", mes_en_curso_real4.shape)

mes_en_curso_real5 = pd.merge(mes_en_curso_real4, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_real5 : ", mes_en_curso_real5.shape)
mes_en_curso_real5.sample(10)


# In[244]:


# TESTING VISUAL 1

mes_en_curso_real5[mes_en_curso_real5["CODIGO_PROYECTO"]=="P-1716"]


# In[245]:


# TESTING VISUAL 3
mes_en_curso_real5[mes_en_curso_real5["CODIGO_PROYECTO"]=="P-1704"]


# In[246]:


# Respaldo de Dataframe mes en curso real
mes_en_curso_real5.to_csv('archivos_respaldo/mes_en_curso_real5.csv', mode='a')


# In[ ]:





# ### 4.4 - **MERGE PARA -> MES EN CURSO ENTRE LIBRO MAYOR + PROYECTADO (PERSPECTIVA MES ANTERIOR)
# (DATAFRAMES: df_libro_mayor5_mec_2M y df_proyectado4) 
# 

# #### 4.4.1 - CREACIÓN DE COPIA DE DATAFRAME "df_libro_mayor5_mec_2M" Y AJUSTES INICIALES
# Ajuste del dataframe proveniente de LIBRO MAYOR

# In[247]:


# Ajuste del dataframe proveniente de LIBRO MAYOR

df_libro_mayor5_mec_2M.sample(5)
df_libro_mayor5_mec_2M_3 = df_libro_mayor5_mec_2M.drop(['CREDITO', 'DEBITO', 'MARGEN'], axis=1)
df_libro_mayor5_mec_2M_3.sample(5)


# In[248]:


# Ajuste del dataframe proveniente de LIBRO MAYOR

df_libro_mayor5_mec_2M.sample(5)
df_libro_mayor5_mec_2M_3 = df_libro_mayor5_mec_2M.drop(['CREDITO', 'DEBITO', 'MARGEN'], axis=1)
df_libro_mayor5_mec_2M_3.sample(5)


# In[249]:


# INSPECCIÓN VISUAL INICIAL 1

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_mec_2M  : ", df_libro_mayor5_mec_2M.shape)
df_libro_mayor5_mec_2M_3[df_libro_mayor5_mec_2M_3["CODIGO_PROYECTO"]=="P-1704"]


# In[250]:


# INSPECCIÓN VISUAL INICIAL

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_mec_2M_3  : ", df_libro_mayor5_mec_2M_3.shape)
df_libro_mayor5_mec_2M_3[df_libro_mayor5_mec_2M_3["CODIGO_PROYECTO"]=="P-1704"]

# Se crea nueva columna que define el destino del uso del trozo del DATAFRAME proveniente del libro mayor

def determinar_origen(row):
    if row['TIPO_CUENTA'] in ['INGRESO', 'COSTO MATERIALES']:
        return 'REAL'
    elif row['TIPO_CUENTA'] in ['COSTO SUPERVISIÓN','COSTO MANO DE OBRA']:
        return 'REAL Y PROYECTADO'

df_libro_mayor5_mec_2M_3['DESTINO'] = df_libro_mayor5_mec_2M_3.apply(determinar_origen, axis=1)
print(df_libro_mayor5_mec_2M_3.shape)
df_libro_mayor5_mec_2M_3.sample(10)


# In[251]:


# Cambiar los valores de la columna TIPO_CUENTA
df_libro_mayor5_mec_2M_3['TIPO_CUENTA'] = df_libro_mayor5_mec_2M_3['TIPO_CUENTA'].replace({'COSTO MATERIALES': '2. COSTO MATERIALES', 'COSTO MANO DE OBRA': '3. COSTO MANO DE OBRA', 'INGRESO': '1. INGRESO','COSTO SUPERVISIÓN': '4. COSTO SUPERVISIÓN'})

print(df_libro_mayor5_mec_2M_3.shape)
df_libro_mayor5_mec_2M_3["TIPO_CUENTA"].unique()


# #### 4.4.2 - CREACIÓN DE COPIA DE DATAFRAME "df_proyectado4" Y AJUSTES INICIALES
# Ajuste del dataframe proveniente de PROYECTADO

# In[252]:


df_proyectado4_1M.sample(5)
df_proyectado5_1M = df_proyectado4_1M.drop(['PROYECTO'], axis=1)

# Se crea la columna Fecha
df_proyectado5_1M['FECHA'] = pd.to_datetime(df_proyectado5_1M['MES'].astype(str) + '-1-' + df_proyectado5_1M['AÑO'].astype(str))

df_proyectado5_1M.sample(5)


# In[253]:


# Se crea nueva columna que define el destino del uso del trozo del DATAFRAME proveniente del proyectado

def determinar_origen(row):
    if row['TIPO_CUENTA'] in ['1. INGRESO', '2. COSTO MATERIALES']:
        return 'PROYECTADO'

# Se realiza 
df_proyectado5_1M['DESTINO'] = df_proyectado5_1M.apply(determinar_origen, axis=1)
df_proyectado5_1M = df_proyectado5_1M[df_proyectado5_1M['TIPO_CUENTA'] != '3. COSTO MANO DE OBRA']


# Se reordenan las columnas para estandarizarlo como la que viene desde Libro Mayot
df_proyectado5_1M = df_proyectado5_1M.reindex(columns=['CODIGO_PROYECTO', 'TIPO_CUENTA', 'FECHA', 'AÑO', 'MES', 'TOTAL', 'ORIGEN', 'DESTINO'])

df_proyectado5_1M.sample(5)


# #### 4.4.3 - CONCATENACIÓN ENTRE DATAFRAMES DEL MES EN CURSO LIBRO MAYOR Y PROYECTADO
# Se realiza concatenación entre ambos dataframes

# In[254]:


print("Dimensiones df_libro_mayor5_mec_2M_3 antes de cambios: ", df_libro_mayor5_mec_2M_3.shape)
print("Dimensiones df_proyectado5_1M antes de cambios       : ", df_proyectado5_1M.shape)

mes_en_curso_2M = pd.concat([df_libro_mayor5_mec_2M_3, df_proyectado5_1M])

print("Dimensiones dataframe final mes_en_curso después de concatenación  : ", mes_en_curso_2M.shape)
mes_en_curso_2M.sample(10)


# #### 4.4.4 - MERGE CON "df_cod_proyecto" PARA CREAR DATAFRAME FINAL

# In[255]:


print("Dimensiones mes_en_curso antes de cambios: ", mes_en_curso_2M.shape)
mes_en_curso_2M = mes_en_curso_2M.merge(df_cod_proyecto, on='CODIGO_PROYECTO', how='left')
mes_en_curso_2M = mes_en_curso_2M[['CODIGO_PROYECTO', 'NOMBRE_OBRA', 'NOMBRE_CLIENTE', 'TIPO_CUENTA', 'FECHA', 'AÑO', 'MES', 'TOTAL', 'ORIGEN', 'DESTINO']]
print("Dimensiones mes_en_curso_2M antes de cambios: ", mes_en_curso_2M.shape)
mes_en_curso_2M.sample(10)


# In[256]:


#Para reemplazar los valores en blanco en las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" por el valor "TOTAL" cada vez que el valor de la columna "CODIGO_PROYECTO" es igual a "TOTAL", puedes hacer lo siguiente:

mes_en_curso_2M.loc[(mes_en_curso_2M['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_2M['NOMBRE_OBRA'].isnull()), 'NOMBRE_OBRA'] = '1. TOTAL'
mes_en_curso_2M.loc[(mes_en_curso_2M['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_2M['NOMBRE_CLIENTE'].isnull()), 'NOMBRE_CLIENTE'] = '1. TOTAL'
mes_en_curso_2M.sample(5)


# In[257]:


# INSPECCIÓN VISUAL 1

mes_en_curso_2M[mes_en_curso_2M["CODIGO_PROYECTO"]=="P-1704"]


# #### 4.3.4 - AGREGACIÓN DE TODOS TIPOS DE CUENTA

# In[258]:


print("Dimensiones Dataframe antes de cambios", mes_en_curso_2M.shape)


# In[259]:


# definir nuevas filas
df_rows_to_add = []

for _, row in mes_en_curso_2M.iterrows():
    if row["TIPO_CUENTA"] == "1. INGRESO" and row["TOTAL"] == 0:
        row1 = row.copy()
        row1["TIPO_CUENTA"] = "1. INGRESO"
        row1["TOTAL"] = 0
        row1["ORIGEN"] = "AGREGACION"
        row1["DESTINO"] = "REAL"
        df_rows_to_add.append(row1)

        row2 = row.copy()
        row2["TIPO_CUENTA"] = "1. INGRESO"
        row2["TOTAL"] = 0
        row2["ORIGEN"] = "AGREGACION"
        row2["DESTINO"] = "PROYECTADO"
        df_rows_to_add.append(row2)

    elif row["TIPO_CUENTA"] == "2. COSTO MATERIALES" and row["TOTAL"] == 0:
        row1 = row.copy()
        row1["TIPO_CUENTA"] = "2. COSTO MATERIALES"
        row1["TOTAL"] = 0
        row1["ORIGEN"] = "AGREGACION"
        row1["DESTINO"] = "REAL"
        df_rows_to_add.append(row1)

        row2 = row.copy()
        row2["TIPO_CUENTA"] = "2. COSTO MATERIALES"
        row2["TOTAL"] = 0
        row2["ORIGEN"] = "AGREGACION"
        row2["DESTINO"] = "PROYECTADO"
        df_rows_to_add.append(row2)

    elif row["TIPO_CUENTA"] == "3. COSTO MANO DE OBRA" and row["TOTAL"] == 0:
        row1 = row.copy()
        row1["TIPO_CUENTA"] = "3. COSTO MANO DE OBRA"
        row1["TOTAL"] = 0
        row1["ORIGEN"] = "AGREGACION"
        row1["DESTINO"] = "REAL Y PROYECTADO"
        df_rows_to_add.append(row1)

  
    elif row["TIPO_CUENTA"] == "4. COSTO SUPERVISIÓN" and row["TOTAL"] == 0:
        row1 = row.copy()
        row1["TIPO_CUENTA"] = "4. COSTO SUPERVISIÓN"
        row1["TOTAL"] = 0
        row1["ORIGEN"] = "AGREGACION"
        row1["DESTINO"] = "REAL Y PROYECTADO"
        df_rows_to_add.append(row1)
        
        row2 = row.copy()
        row2["TIPO_CUENTA"] = "3. COSTO MANO DE OBRA"
        row2["TOTAL"] = 0
        row2["ORIGEN"] = "AGREGACION"
        row2["DESTINO"] = "REAL Y PROYECTADO"
        df_rows_to_add.append(row2)


# In[260]:


# concatenar nuevas filas al DataFrame original
mes_en_curso_2M = pd.concat([mes_en_curso_2M, pd.DataFrame(df_rows_to_add)], ignore_index=True)


# In[261]:


# Se renombra "TOTAL" a "1. TOTAL" para que se pueda visualizar como primera opción en el dashboard.
mes_en_curso_2M['CODIGO_PROYECTO'] = mes_en_curso_2M['CODIGO_PROYECTO'].apply(lambda x: '1. TOTAL' if x == 'TOTAL' else x)

cols_to_replace = ['CODIGO_PROYECTO', 'NOMBRE_OBRA', 'NOMBRE_CLIENTE']
mes_en_curso_2M[cols_to_replace] = mes_en_curso_2M[cols_to_replace].replace('TOTAL', '1. TOTAL')
mask = mes_en_curso_2M['CODIGO_PROYECTO'] == '1. TOTAL'
mes_en_curso_2M.loc[mask, ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

print("Dimensiones Dataframe después de cambios", mes_en_curso_2M.shape)

mes_en_curso_2M.sample(10)


# In[262]:


# INSPECCIÓN VISUAL 1
mes_en_curso_2M[mes_en_curso_2M["CODIGO_PROYECTO"]=="P-1726"]


# In[263]:


mes_en_curso_2M["TIPO_CUENTA"].unique()


# In[264]:


# INSPECCIÓN VISUAL 1
mes_en_curso_2M[mes_en_curso_2M["CODIGO_PROYECTO"]=="1. TOTAL"]


# #### 4.4.7 - **CREACIÓN DATAFRAME PARA -> PROYECTADO

# In[265]:


# Se crea una copia del dataframe original mes_en_curso2

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_2M       : ", mes_en_curso_2M.shape)

mes_en_curso_2M_1 = mes_en_curso_2M.copy()
mes_en_curso_2M_1 = mes_en_curso_2M_1[mes_en_curso_2M_1['DESTINO'].str.contains('PROYECTADO')]

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_2M_1   : ", mes_en_curso_2M_1.shape)


print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_2M_1     : ", mes_en_curso_2M_1.shape)

mes_en_curso_proy_2M = pd.pivot_table(mes_en_curso_2M_1, values=['TOTAL'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum', fill_value=0)
mes_en_curso_proy_2M = pd.DataFrame(mes_en_curso_proy_2M.to_records())

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_proy_2M  : ", mes_en_curso_proy_2M.shape)

mes_en_curso_proy_2M.sample(10)


# In[266]:


# TESTING VISUAL 1
mes_en_curso_proy_2M[mes_en_curso_proy_2M["CODIGO_PROYECTO"]=="P-1726"]


# In[267]:


# TESTING VISUAL 2
mes_en_curso_proy_2M[mes_en_curso_proy_2M["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.4.7.1 - MERGE CON DATAFRAME LIBRO MAYOR 2023 BASE 

# In[268]:


# Merge Dataframe BASE 

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_proy_2M     : ", mes_en_curso_proy_2M.shape)
print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_base2    : ", df_libro_mayor5_base2.shape)

mes_en_curso_proy_2M_2 = df_libro_mayor5_base2.merge(mes_en_curso_proy_2M, on=['CODIGO_PROYECTO', 'TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_proy_2M_2  : ", mes_en_curso_proy_2M_2.shape)

mes_en_curso_proy_2M_2['TOTAL'] = mes_en_curso_proy_2M_2['TOTAL'].fillna(0)

mes_en_curso_proy_2M_2.sample(5)


# In[269]:


# TESTING VISUAL 1

mes_en_curso_proy_2M_2[mes_en_curso_proy_2M_2["CODIGO_PROYECTO"]=="P-1726"]


# In[270]:


# TESTING VISUAL 2
mes_en_curso_proy_2M_2[mes_en_curso_proy_2M_2["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.4.7.2 - SE RECALCULAN LOS TOTALES

# In[271]:


# Calcular la suma de los valores totales para cada tipo de cuenta

# Se eliminan totales excepto supervisión, para re hacer el calculo de totales

mes_en_curso_proy_2M_2 = mes_en_curso_proy_2M_2.drop(mes_en_curso_proy_2M_2[(mes_en_curso_proy_2M_2['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_proy_2M_2['TIPO_CUENTA'] != '4. COSTO SUPERVISIÓN')].index)

print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_proy_2M_2 : ", mes_en_curso_proy_2M_2.shape)

df_total = mes_en_curso_proy_2M_2.groupby('TIPO_CUENTA')['TOTAL'].sum().reset_index()
df_total['CODIGO_PROYECTO'] = '1. TOTAL'

# Agregar las filas adicionales al DataFrame
mes_en_curso_proy_2M_3 = pd.concat([mes_en_curso_proy_2M_2, df_total], ignore_index=True)

# Modificar las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" para "1. TOTAL"
mes_en_curso_proy_2M_3.loc[mes_en_curso_proy_2M_3['CODIGO_PROYECTO'] == '1. TOTAL', ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_proy_2M_3 : ", mes_en_curso_proy_2M_3.shape)

mes_en_curso_proy_2M_3.sample(10) 


# In[272]:


# TESTING VISUAL 2
mes_en_curso_proy_2M_3[mes_en_curso_proy_2M_3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[273]:


# SE ELIMINA COSTO SUPERVISIÓN DUPLICADO.

print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_proy_2M_3 : ", mes_en_curso_proy_2M_3.shape)

mes_en_curso_proy_2M_3 = mes_en_curso_proy_2M_3.drop(mes_en_curso_proy_2M_3[(mes_en_curso_proy_2M_3['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_proy_2M_3['TIPO_CUENTA'] == '4. COSTO SUPERVISIÓN') & (mes_en_curso_proy_2M_3['TOTAL_LB'].isnull())].index)

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_proy_2M_3 : ", mes_en_curso_proy_2M_3.shape)

mes_en_curso_proy_2M_3[mes_en_curso_proy_2M_3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[274]:


# TESTING VISUAL 1
mes_en_curso_proy_2M_3[mes_en_curso_proy_2M_3["CODIGO_PROYECTO"]=="P-1726"]


# In[275]:


# TESTING VISUAL 2
mes_en_curso_proy_2M_3[mes_en_curso_proy_2M_3["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.4.7.3 - CREACIÓN DE MARGEN

# In[276]:


#CREACIÓN DE MARGENES

mes_en_curso_proy_2M_4 = mes_en_curso_proy_2M_3.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = mes_en_curso_proy_2M_4.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


# In[277]:


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_proy_2M_4 : ", mes_en_curso_proy_2M_4.shape)

mes_en_curso_proy_2M_5 = pd.merge(mes_en_curso_proy_2M_4, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_proy_2M_5 : ", mes_en_curso_proy_2M_5.shape)
mes_en_curso_proy_2M_5.sample(10)


# In[278]:


# TESTING VISUAL 1
mes_en_curso_proy_2M_5[mes_en_curso_proy_2M_5["CODIGO_PROYECTO"]=="P-1723"]


# In[279]:


# TESTING VISUAL 2
mes_en_curso_proy_2M_5[mes_en_curso_proy_2M_5["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[280]:


# Respaldo de Dataframe mes en curso antes de abrirrlo
mes_en_curso_proy_2M_5.to_csv('archivos_respaldo/mes_en_curso_proy_2M_5.csv', mode='a')


# In[281]:


mes_en_curso_proy_2M_5[mes_en_curso_proy_2M_5["CODIGO_PROYECTO"]=="P-1726"]


# In[ ]:





# #### 4.4.8 - **CREACIÓN DATAFRAME PARA -> MES EN CURSO (PERSPECTIVA MES ANTERIOR)

# ##### 4.4.8.1 - TRATAMIENTO mes_en_curso2

# In[282]:


# Se crea una copia del dataframe original mes_en_curso2

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_2M       : ", mes_en_curso_2M.shape)

mes_en_curso_2M_1 = mes_en_curso_2M.copy()
mes_en_curso_2M_1 = mes_en_curso_2M_1[mes_en_curso_2M_1['DESTINO'].str.contains('REAL')]

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_2M_1     : ", mes_en_curso_2M_1.shape)

mes_en_curso_real_2M = pd.pivot_table(mes_en_curso_2M_1, values=['TOTAL'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum', fill_value=0)
mes_en_curso_real_2M = pd.DataFrame(mes_en_curso_real_2M.to_records())

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_real_2M  : ", mes_en_curso_real_2M.shape)

mes_en_curso_real_2M.sample(10)


# In[283]:


# TESTING VISUAL 1

mes_en_curso_real_2M[mes_en_curso_real_2M["CODIGO_PROYECTO"]=="P-1712"]


# In[284]:


# TESTING VISUAL 2

mes_en_curso_real_2M[mes_en_curso_real_2M["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.4.8.2 - MERGE CON DATAFRAME LIBRO MAYOR 2023 BASE 

# In[285]:


# Merge Dataframe BASE 

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_real_2M    : ", mes_en_curso_real_2M.shape)
print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME: df_libro_mayor5_base2   : ", df_libro_mayor5_base2.shape)

mes_en_curso_real_2M = df_libro_mayor5_base2.merge(mes_en_curso_real_2M, on=['CODIGO_PROYECTO', 'TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_real_2M   : ", mes_en_curso_real_2M.shape)

mes_en_curso_real_2M.sample(5)


# In[286]:


# TESTING VISUAL 1

mes_en_curso_real_2M[mes_en_curso_real_2M["CODIGO_PROYECTO"]=="P-1712"]


# In[287]:


# TESTING VISUAL 2

mes_en_curso_real_2M[mes_en_curso_real_2M["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.4.8.3 - SE RECALCULAN LOS TOTALES

# In[288]:


# Calcular la suma de los valores totales para cada tipo de cuenta

# Se eliminan totales excepto supervisión, para re hacer el calculo de totales

mes_en_curso_real_2M = mes_en_curso_real_2M.drop(mes_en_curso_real_2M[(mes_en_curso_real_2M['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_real_2M['TIPO_CUENTA'] != '4. COSTO SUPERVISIÓN')].index)

print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_real_2M : ", mes_en_curso_real_2M.shape)

df_total = mes_en_curso_real_2M.groupby('TIPO_CUENTA')['TOTAL'].sum().reset_index()
df_total['CODIGO_PROYECTO'] = '1. TOTAL'

# Agregar las filas adicionales al DataFrame
mes_en_curso_real_2M_3 = pd.concat([mes_en_curso_real_2M, df_total], ignore_index=True)

# Modificar las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" para "1. TOTAL"
mes_en_curso_real_2M_3.loc[mes_en_curso_real_2M_3['CODIGO_PROYECTO'] == '1. TOTAL', ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_real_2M_3 : ", mes_en_curso_real_2M_3.shape)

mes_en_curso_real_2M_3.sample(10)  


# In[289]:


# TESTING VISUAL 1

mes_en_curso_real_2M_3[mes_en_curso_real_2M_3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[290]:


# SE ELIMINA COSTO SUPERVISIÓN DUPLICADO.

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: mes_en_curso_real_2M_3 : ", mes_en_curso_real_2M_3.shape)

mes_en_curso_real_2M_3 = mes_en_curso_real_2M_3.drop(mes_en_curso_real_2M_3[(mes_en_curso_real_2M_3['CODIGO_PROYECTO'] == '1. TOTAL') & (mes_en_curso_real_2M_3['TIPO_CUENTA'] == '4. COSTO SUPERVISIÓN') & (mes_en_curso_real_2M_3['TOTAL_LB'].isnull())].index)

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_real_2M_3 : ", mes_en_curso_real_2M_3.shape)

mes_en_curso_real_2M_3[mes_en_curso_real_2M_3["CODIGO_PROYECTO"]=="1. TOTAL"]


# ##### 4.4.8.4 - CREACIÓN DE MARGEN

# In[291]:


#CREACIÓN DE MARGENES

mes_en_curso_real_2M_4 = mes_en_curso_real_2M_3.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = mes_en_curso_real_2M_4.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


# In[292]:


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_real_2M_4 : ", mes_en_curso_real_2M_4.shape)

mes_en_curso_real_2M_5 = pd.merge(mes_en_curso_real_2M_4, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: mes_en_curso_real_2M_5 : ", mes_en_curso_real_2M_5.shape)
mes_en_curso_real_2M_5.sample(10)


# In[293]:


# TESTING VISUAL 1
mes_en_curso_real_2M_5[mes_en_curso_real_2M_5["CODIGO_PROYECTO"]=="P-1716"]


# In[294]:


# TESTING VISUAL 2
mes_en_curso_real_2M_5[mes_en_curso_real_2M_5["CODIGO_PROYECTO"]=="P-1704"]


# In[295]:


# Respaldo de Dataframe mes en curso real
mes_en_curso_real_2M_5.to_csv('archivos_respaldo/mes_en_curso_real_2M_5.csv', mode='a')


# In[ ]:





# ### 4.5 - **MERGE PARA -> YTD PROYECTADO
# YTD Proyectado = YTD + el mes en curso del proyectado

# #### 4.5.1 - EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES
# 

# In[296]:


# DATAFRAME PROVENIENTE DEL LIBRO MAYOR 2023 HASTA EL MES CERRADO.

print(df_ytd_cerrado.shape)
df_ytd_cerrado.sample(10)


# In[297]:


# DATAFRAME PROVENIENTE DEL LIBRO PERO SOO CONSIDERA MES EN CURSO.

print(mes_en_curso2.shape)
mes_en_curso2.head(5)

# Se filtra por la columna DESTINO != REAL (para considerar solo lo proyectado)
mes_en_curso2_1 = mes_en_curso2[mes_en_curso2['DESTINO'] != 'REAL']

# Eliminar las columnas ORIGEN y DESTINO
mes_en_curso2_1 = mes_en_curso2_1.drop(columns=['ORIGEN', 'DESTINO','MES','AÑO','FECHA'])

mes_en_curso2_1.sample(5)


# #### 4.5.2 - Concatenación de Dataframes

# In[298]:


# Se concatenan los dataframes.

print("Dataframes antes de concatenar   : df_ytd_cerrado   ", df_ytd_cerrado.shape)
print("Dataframes antes de concatenar   : mes_en_curso2_1  ", mes_en_curso2_1.shape)

df_ytd_proyectado = pd.concat([df_ytd_cerrado, mes_en_curso2_1], axis=0)
print("Dataframes después de concatenar : df_ytd_proyectado  ", df_ytd_proyectado.shape)

df_ytd_proyectado.sample(5)


# In[299]:


df_ytd_proyectado["CODIGO_PROYECTO"].unique()


# In[300]:


# TESTING VISUAL 1 

df_ytd_proyectado[df_ytd_proyectado["CODIGO_PROYECTO"] == "P-1727"]


# In[301]:


# TESTING VISUAL 2

df_ytd_proyectado[df_ytd_proyectado["CODIGO_PROYECTO"] == "1. TOTAL"]


# #### 4.5.3 - AGREGACIÓN COLUMNA MARGEN

# In[302]:


#CREACIÓN DE MARGENES

df_ytd_proyectado2 = df_ytd_proyectado.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_ytd_proyectado2.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: mes_en_curso_real4 : ", df_ytd_proyectado2.shape)

df_ytd_proyectado2 = pd.merge(df_ytd_proyectado2, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ytd_proyectado2 : ", df_ytd_proyectado2.shape)
df_ytd_proyectado2.sample(10)


# In[303]:


# TESTING VISUAL 1 

df_ytd_proyectado2[df_ytd_proyectado2["CODIGO_PROYECTO"] == "P-1727"]


# In[304]:


# TESTING VISUAL 2

df_ytd_proyectado2[df_ytd_proyectado2["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[305]:


# Respaldo de Dataframe mes en curso real

df_ytd_proyectado2.to_csv('archivos_respaldo/df_ytd_proyectado2.csv', mode='a')


# In[ ]:





# ### 4.6 - **MERGE PARA -> YTD PROYECTADO (PERSPECTIVA MES ANTERIOR)
# YTD Proyectado = YTD + el mes en curso del proyectado

# #### 4.6.1 - EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES
# 

# In[306]:


# DATAFRAME PROVENIENTE DEL LIBRO MAYOR 2023 HASTA EL MES CERRADO.

print(df_ytd_cerrado_2M.shape)
df_ytd_cerrado_2M.sample(10)


# In[307]:


# DATAFRAME PROVENIENTE DEL LIBRO PERO SOO CONSIDERA MES EN CURSO.

print(mes_en_curso_2M.shape)
mes_en_curso_2M.head(5)

# Se filtra por la columna DESTINO != REAL (para considerar solo lo proyectado)#
mes_en_curso_proy_2M_2_1 = mes_en_curso_2M[mes_en_curso_2M['DESTINO'] != 'REAL']

# Eliminar las columnas ORIGEN y DESTINO
mes_en_curso_proy_2M_2_1 = mes_en_curso_proy_2M_2_1.drop(columns=['ORIGEN', 'DESTINO','MES','AÑO','FECHA'])

mes_en_curso_proy_2M_2_1.sample(5)


# In[308]:


# TESTING VISUAL 1 

mes_en_curso_proy_2M_2_1[mes_en_curso_proy_2M_2_1["CODIGO_PROYECTO"] == "1. TOTAL"]


# #### 4.6.2 - Concatenación de Dataframes

# In[309]:


# Se concatenan los dataframes.

print("Dataframes antes de concatenar   : df_ytd_cerrado_2M       :", df_ytd_cerrado_2M.shape)
print("Dataframes antes de concatenar   : mes_en_curso_proy_2M_2_1:", mes_en_curso_proy_2M_2_1.shape)

df_ytd_proyectado_2M = pd.concat([df_ytd_cerrado_2M, mes_en_curso_proy_2M_2_1], axis=0)
print("Dataframes después de concatenar : df_ytd_proyectado_2M  ", df_ytd_proyectado_2M.shape)

df_ytd_proyectado_2M.sample(5)


# In[310]:


df_ytd_proyectado_2M["CODIGO_PROYECTO"].unique()


# In[311]:


# TESTING VISUAL 1 

df_ytd_proyectado_2M[df_ytd_proyectado_2M["CODIGO_PROYECTO"] == "P-1727"]


# In[312]:


# TESTING VISUAL 2

df_ytd_proyectado_2M[df_ytd_proyectado_2M["CODIGO_PROYECTO"] == "1. TOTAL"]


# #### 4.6.3 - AGREGACIÓN COLUMNA MARGEN

# In[313]:


#CREACIÓN DE MARGENES

df_ytd_proyectado_2M_2 = df_ytd_proyectado_2M.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_ytd_proyectado_2M_2.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_ytd_proyectado_2M_2 : ", df_ytd_proyectado_2M_2.shape)

df_ytd_proyectado_2M_2 = pd.merge(df_ytd_proyectado_2M_2, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ytd_proyectado_2M_2 : ", df_ytd_proyectado_2M_2.shape)
df_ytd_proyectado_2M_2.sample(10)


# In[314]:


# TESTING VISUAL 1 

df_ytd_proyectado_2M_2[df_ytd_proyectado_2M_2["CODIGO_PROYECTO"] == "P-1727"]


# In[315]:


# Respaldo de Dataframe mes en curso real

df_ytd_proyectado_2M_2.to_csv('archivos_respaldo/df_ytd_proyectado_2M_2.csv', mode='a')


# In[ ]:





# ### 4.7 - **MERGE PARA -> PTD CERRADO

# Cruce entre YTD_Cerrado + Libros mayores de años anteriores.

# #### 4.7.1 - EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[316]:


# Exploración Dataframe para el dataframe que proviene del Libro Mayor 2023.
# Dataframe : df_ytd_cerrado2 proveniente del punto 4.2 - MERGE PARA -> YTD AÑO EN CURSO HASTA MES CERRADO

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ytd_cerrado2 : ", df_ytd_cerrado2.shape)

df_ytd_cerrado_1 = df_ytd_cerrado2.copy()
df_ytd_cerrado_1.sample(5)


# In[317]:


# TESTING VISUAL 1

print(df_ytd_cerrado_1[df_ytd_cerrado_1["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ytd_cerrado_1[df_ytd_cerrado_1["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[318]:


# Se crea Pivote para reducir las dimensiones

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ytd_cerrado_1 : ", df_ytd_cerrado_1.shape)
df_ytd_cerrado_2 = pd.pivot_table(df_ytd_cerrado_1, values=['TOTAL'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ytd_cerrado_2 : ", df_ytd_cerrado_2.shape)

# Se renombra campo "TOTAL"
df_ytd_cerrado_2 = df_ytd_cerrado_2.rename(columns={"TOTAL": "TOTAL YTD"})

df_ytd_cerrado_2 = pd.DataFrame(df_ytd_cerrado_2.to_records())
df_ytd_cerrado_2.sample(10)


# In[ ]:





# In[319]:


# Exploración y tratamiento de dataframe: df_ytd_cerrado df_libro_mayor_old3

# Se crea una copia del dataframe 
print("Dimensiones del dataframe df_libro_mayor_old3 : ", df_libro_mayor_old3.shape)
df_libro_mayor_old4 = df_libro_mayor_old3.copy()
print("Dimensiones del dataframe df_libro_mayor_old4 : ", df_libro_mayor_old4.shape)
df_libro_mayor_old4.sample(10)


# In[320]:


# Se realiza limpieza del dataframe para obtener solo las columnas utiles.

df_libro_mayor_old4 = df_libro_mayor_old4[df_libro_mayor_old4['CODIGO_PROYECTO'] != '']
df_libro_mayor_old4 = df_libro_mayor_old4[df_libro_mayor_old4['TIPO_CUENTA'] != 'OTRA']
df_libro_mayor_old4 = df_libro_mayor_old4[df_libro_mayor_old4['TIPO_CUENTA'] != '']
df_libro_mayor_old4 = df_libro_mayor_old4.dropna(subset=['TIPO_CUENTA'])
df_libro_mayor_old4 = df_libro_mayor_old4.dropna(subset=['CODIGO_PROYECTO'])

print("Dimensiones del dataframe df_libro_mayor_old4 : ", df_libro_mayor_old4.shape)
df_libro_mayor_old4.sample(10)


# In[321]:


# TESTING VISUAL 1

print(df_libro_mayor_old4[df_libro_mayor_old4["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_libro_mayor_old4[df_libro_mayor_old4["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[322]:


# Se crea Pivote para reducir las dimensiones

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_libro_mayor_old4 : ", df_libro_mayor_old4.shape)
df_libro_mayor_old5 = pd.pivot_table(df_libro_mayor_old4, values=['TOTAL'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum')

# Se renombra campo "TOTAL"
df_libro_mayor_old5 = df_libro_mayor_old5.rename(columns={"TOTAL": "TOTAL LB OLD"})

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_libro_mayor_old5 : ", df_libro_mayor_old5.shape)

df_libro_mayor_old5 = pd.DataFrame(df_libro_mayor_old5.to_records())
df_libro_mayor_old5.sample(10)


# In[323]:


# TESTING VISUAL 1

print(df_libro_mayor_old5[df_libro_mayor_old5["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL LB OLD"].sum())
df_libro_mayor_old5[df_libro_mayor_old5["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[324]:


# TESTING VISUAL 2

print(df_libro_mayor_old5[df_libro_mayor_old5["CODIGO_PROYECTO"] == "P-1615"]["TOTAL LB OLD"].sum())
df_libro_mayor_old5[df_libro_mayor_old5["CODIGO_PROYECTO"] == "P-1615"].head(5)


# In[ ]:





# #### 4.7.2 - Concatenación de Dataframes

# In[325]:


# Se considera df_libro_mayor5_base2 como base para construir el dataframe

df_ptd_cerrado = df_libro_mayor5_base2.copy()

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado : ", df_ptd_cerrado.shape)
df_ptd_cerrado.sample(5)


# In[326]:


# MERGE 1 - df_ytd_cerrado2

# Se hace merge con los codigos de proyecto.

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_pendiente2 : ", df_ptd_cerrado.shape)

df_ptd_cerrado = pd.merge(df_ptd_cerrado, df_ytd_cerrado_2, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado : ", df_ptd_cerrado.shape)

df_ptd_cerrado.sample(10)


# In[327]:


# MERGE 2 - df_ytd_cerrado2

# Se hace merge con los codigos de proyecto.

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado : ", df_ptd_cerrado.shape)

df_ptd_cerrado = pd.merge(df_ptd_cerrado, df_libro_mayor_old5, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado : ", df_ptd_cerrado.shape)

df_ptd_cerrado.sample(10)


# In[328]:


# Se estandarizan columnas de Totales y se agrega columna TOTAL 

# Reemplazar NaN por cero en las columnas "TOTAL YTD" y "TOTAL LB OLD"
df_ptd_cerrado["TOTAL YTD"] = df_ptd_cerrado["TOTAL YTD"].fillna(0)
df_ptd_cerrado["TOTAL LB OLD"] = df_ptd_cerrado["TOTAL LB OLD"].fillna(0)

# Crear la nueva columna "TOTAL" que suma "TOTAL YTD" y "TOTAL LB OLD"
df_ptd_cerrado["TOTAL"] = df_ptd_cerrado["TOTAL YTD"] + df_ptd_cerrado["TOTAL LB OLD"]
df_ptd_cerrado.sample(5)


# In[329]:


# TESTING VISUAL 1

print(df_ptd_cerrado[df_ptd_cerrado["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL YTD"].sum())
print(df_ptd_cerrado[df_ptd_cerrado["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL LB OLD"].sum())
print(df_ptd_cerrado[df_ptd_cerrado["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())

df_ptd_cerrado[df_ptd_cerrado["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[330]:


# TESTING VISUAL 2

print(df_ptd_cerrado[df_ptd_cerrado["CODIGO_PROYECTO"] == "P-1727"]["TOTAL YTD"].sum())
print(df_ptd_cerrado[df_ptd_cerrado["CODIGO_PROYECTO"] == "P-1727"]["TOTAL LB OLD"].sum())
print(df_ptd_cerrado[df_ptd_cerrado["CODIGO_PROYECTO"] == "P-1727"]["TOTAL"].sum())

df_ptd_cerrado[df_ptd_cerrado["CODIGO_PROYECTO"] == "P-1727"]


# #### 4.7.3 - SE AGREGAN FILAS DE 1.TOTAL

# In[331]:


# Se eliminan Totales, excepto cuando se trata de COSTO_SUPERVISIÓN

print("DIMENSIONES ANTES DE TRATAMIENTO DEL DATAFRAME: df_ptd_cerrado : ", df_ptd_cerrado.shape)

df_ptd_cerrado2 = df_ptd_cerrado[~((df_ptd_cerrado["CODIGO_PROYECTO"] == "1. TOTAL") & (df_ptd_cerrado["TIPO_CUENTA"] != "4. COSTO SUPERVISIÓN"))]

print("DIMENSIONES DESPUÉS DE TRATAMIENTO DEL DATAFRAME df_ptd_cerrado2 : ", df_ptd_cerrado2.shape)


# In[332]:


# TESTING VISUAL 2


print(df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL YTD"].sum())
print(df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL LB OLD"].sum())
print(df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())

df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[333]:


# Calcular la suma de los valores totales para cada tipo de cuenta

print("DIMENSIONES ANTES DE TRATAMIENTO DEL DATAFRAME: df_ptd_cerrado2 : ", df_ptd_cerrado2.shape)

df_total = df_ptd_cerrado2.groupby('TIPO_CUENTA')['TOTAL'].sum().reset_index()
df_total['CODIGO_PROYECTO'] = '1. TOTAL'

# Agregar las filas adicionales al DataFrame
df_ptd_cerrado2 = pd.concat([df_ptd_cerrado2, df_total], ignore_index=True)

# Modificar las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" para "1. TOTAL"
df_ptd_cerrado2.loc[df_ptd_cerrado2['CODIGO_PROYECTO'] == '1. TOTAL', ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

print("DIMENSIONES DESPUÉS DE TRATAMIENTO DEL DATAFRAME df_ptd_cerrado2 : ", df_ptd_cerrado2.shape)

df_ptd_cerrado2.sample(5)  


# In[334]:


# TESTING VISUAL 1

print(df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[335]:


# Se eliminan COSTO SUPERVISION INCORRECTO

df_ptd_cerrado2 = df_ptd_cerrado2[~((df_ptd_cerrado2['CODIGO_PROYECTO'] == '1. TOTAL') & (df_ptd_cerrado2['TIPO_CUENTA'] == '4. COSTO SUPERVISIÓN') & (df_ptd_cerrado2['TOTAL_LB'].isna()))]
 
# TESTING VISUAL 2

print(df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[336]:


# TESTING VISUAL 2

print(df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "P-1727"]["TOTAL"].sum())
df_ptd_cerrado2[df_ptd_cerrado2["CODIGO_PROYECTO"] == "P-1727"].head(5)


# #### 4.7.4 - AGREGACIÓN COLUMNA MARGEN

# In[337]:


#CREACIÓN DE MARGENES

df_ptd_cerrado3 = df_ptd_cerrado2.copy()


# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_ptd_cerrado3.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_ptd_cerrado3 : ", df_ptd_cerrado3.shape)

df_ptd_cerrado3 = pd.merge(df_ptd_cerrado3, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado3 : ", df_ptd_cerrado3.shape)
df_ptd_cerrado3.sample(5)


# In[338]:


# TESTING VISUAL 1

print(df_ptd_cerrado3[df_ptd_cerrado3["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado3[df_ptd_cerrado3["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[339]:


# TESTING VISUAL 2

print(df_ptd_cerrado3[df_ptd_cerrado3["CODIGO_PROYECTO"] == "P-1727"]["TOTAL"].sum())
df_ptd_cerrado3[df_ptd_cerrado3["CODIGO_PROYECTO"] == "P-1727"].head(5)


# In[340]:


df_ptd_cerrado3.to_csv('archivos_respaldo/df_ptd_cerrado3.csv', index = False)


# In[ ]:





# ### 4.8 - **MERGE PARA -> PTD CERRADO (PERSPECTIVA MES ANTERIOR)
# Cruce entre YTD_Cerrado + Libros mayores de años anteriores.

# #### 4.8.1 - EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[341]:


# Exploración Dataframe para el dataframe que proviene del Libro Mayor 2023.
# Dataframe : df_ytd_cerrado2 proveniente del punto 4.3 - MERGE PARA -> YTD AÑO EN CURSO HASTA MES CERRADO PERSPECTIVA MES ANTERIOR

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ytd_cerrado_2M_3 : ", df_ytd_cerrado_2M_3.shape)

df_ytd_cerrado_2M_3_1 = df_ytd_cerrado_2M_3.copy()
df_ytd_cerrado_2M_3_1.sample(5)


# In[342]:


# TESTING VISUAL 1

print(df_ytd_cerrado_2M_3_1[df_ytd_cerrado_2M_3_1["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ytd_cerrado_2M_3_1[df_ytd_cerrado_2M_3_1["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[343]:


# Se crea Pivote para reducir las dimensiones

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ytd_cerrado_2M_3_1   : ", df_ytd_cerrado_2M_3_1.shape)
df_ytd_cerrado_2M_3_2 = pd.pivot_table(df_ytd_cerrado_2M_3_1, values=['TOTAL'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ytd_cerrado_2M_3_2 : ", df_ytd_cerrado_2M_3_2.shape)

# Se renombra campo "TOTAL"
df_ytd_cerrado_2M_3_2 = df_ytd_cerrado_2M_3_2.rename(columns={"TOTAL": "TOTAL YTD"})

df_ytd_cerrado_2M_3_2 = pd.DataFrame(df_ytd_cerrado_2M_3_2.to_records())
df_ytd_cerrado_2M_3_2.sample(10)


# In[344]:


# Exploración y tratamiento de dataframe: df_ytd_cerrado df_libro_mayor_old3
# Se utiliza el dataframe creado previamente en el punto: 4.7.1 : df_libro_mayor_old5 (NO ES NECESARIO TRATAR NUEVAMENTE LOS DATOS DEL LIBRO MAYOR DE AÑOS ANTRIORES)

print("Dimensiones del dataframe df_libro_mayor_old5 : ", df_libro_mayor_old5.shape)
df_libro_mayor_old5.sample(10)


# #### 4.8.2 - Concatenación de Dataframes

# In[345]:


# Se considera df_libro_mayor5_base2 como base para construir el dataframe

df_ptd_cerrado_anterior = df_libro_mayor5_base2.copy()

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado_anterior : ", df_ptd_cerrado_anterior.shape)
df_ptd_cerrado_anterior.sample(5)


# In[346]:


# MERGE 1 - df_ytd_cerrado_2M_3_2

# Se hace merge con los codigos de proyecto.

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ytd_cerrado_2M_3_2 : ", df_ytd_cerrado_2M_3_2.shape)

df_ptd_cerrado_anterior = pd.merge(df_ptd_cerrado_anterior, df_ytd_cerrado_2M_3_2, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado_anterior : ", df_ptd_cerrado_anterior.shape)

df_ptd_cerrado_anterior.sample(10)


# In[347]:


# MERGE 2 - df_ytd_cerrado2

# Se hace merge con los codigos de proyecto.

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado_anterior : ", df_ptd_cerrado_anterior.shape)

df_ptd_cerrado_anterior = pd.merge(df_ptd_cerrado_anterior, df_libro_mayor_old5, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado_anterior : ", df_ptd_cerrado_anterior.shape)

df_ptd_cerrado_anterior.sample(10)


# In[348]:


# Se estandarizan columnas de Totales y se agrega columna TOTAL 

# Reemplazar NaN por cero en las columnas "TOTAL YTD" y "TOTAL LB OLD"
df_ptd_cerrado_anterior["TOTAL YTD"] = df_ptd_cerrado_anterior["TOTAL YTD"].fillna(0)
df_ptd_cerrado_anterior["TOTAL LB OLD"] = df_ptd_cerrado_anterior["TOTAL LB OLD"].fillna(0)

# Crear la nueva columna "TOTAL" que suma "TOTAL YTD" y "TOTAL LB OLD"
df_ptd_cerrado_anterior["TOTAL"] = df_ptd_cerrado_anterior["TOTAL YTD"] + df_ptd_cerrado_anterior["TOTAL LB OLD"]
df_ptd_cerrado_anterior.sample(5)


# In[349]:


# TESTING VISUAL 1

print(df_ptd_cerrado_anterior[df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL YTD"].sum())
print(df_ptd_cerrado_anterior[df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL LB OLD"].sum())
print(df_ptd_cerrado_anterior[df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())

df_ptd_cerrado_anterior[df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[350]:


# TESTING VISUAL 2

print(df_ptd_cerrado_anterior[df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "P-1704"]["TOTAL YTD"].sum())
print(df_ptd_cerrado_anterior[df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "P-1704"]["TOTAL LB OLD"].sum())
print(df_ptd_cerrado_anterior[df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "P-1704"]["TOTAL"].sum())

df_ptd_cerrado_anterior[df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "P-1704"]


# #### 4.8.3 - SE AGREGAN FILAS DE 1.TOTAL

# In[351]:


# Se eliminan Totales, excepto cuando se trata de COSTO_SUPERVISIÓN

print("DIMENSIONES ANTES DE TRATAMIENTO DEL DATAFRAME: df_ptd_cerrado_anterior : ", df_ptd_cerrado_anterior.shape)

df_ptd_cerrado_anterior2 = df_ptd_cerrado_anterior[~((df_ptd_cerrado_anterior["CODIGO_PROYECTO"] == "1. TOTAL") & (df_ptd_cerrado_anterior["TIPO_CUENTA"] != "4. COSTO SUPERVISIÓN"))]

print("DIMENSIONES DESPUÉS DE TRATAMIENTO DEL DATAFRAME df_ptd_cerrado_anterior2 : ", df_ptd_cerrado_anterior2.shape)


# In[352]:


# TESTING VISUAL 2


print(df_ptd_cerrado_anterior2[df_ptd_cerrado_anterior2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL YTD"].sum())
print(df_ptd_cerrado_anterior2[df_ptd_cerrado_anterior2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL LB OLD"].sum())
print(df_ptd_cerrado_anterior2[df_ptd_cerrado_anterior2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())

df_ptd_cerrado_anterior2[df_ptd_cerrado_anterior2["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[353]:


# Calcular la suma de los valores totales para cada tipo de cuenta

print("DIMENSIONES ANTES DE TRATAMIENTO DEL DATAFRAME: df_ptd_cerrado_anterior2 : ", df_ptd_cerrado_anterior2.shape)

df_total = df_ptd_cerrado_anterior2.groupby('TIPO_CUENTA')['TOTAL'].sum().reset_index()
df_total['CODIGO_PROYECTO'] = '1. TOTAL'

# Agregar las filas adicionales al DataFrame
df_ptd_cerrado_anterior2 = pd.concat([df_ptd_cerrado_anterior2, df_total], ignore_index=True)

# Modificar las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" para "1. TOTAL"
df_ptd_cerrado_anterior2.loc[df_ptd_cerrado_anterior2['CODIGO_PROYECTO'] == '1. TOTAL', ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

print("DIMENSIONES DESPUÉS DE TRATAMIENTO DEL DATAFRAME df_ptd_cerrado_anterior2 : ", df_ptd_cerrado_anterior2.shape)

df_ptd_cerrado_anterior2.sample(5)  


# In[354]:


# TESTING VISUAL 1

print(df_ptd_cerrado_anterior2[df_ptd_cerrado_anterior2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado_anterior2[df_ptd_cerrado_anterior2["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[355]:


# Se eliminan COSTO SUPERVISION INCORRECTO

df_ptd_cerrado_anterior2 = df_ptd_cerrado_anterior2[~((df_ptd_cerrado_anterior2['CODIGO_PROYECTO'] == '1. TOTAL') & (df_ptd_cerrado_anterior2['TIPO_CUENTA'] == '4. COSTO SUPERVISIÓN') & (df_ptd_cerrado_anterior2['TOTAL_LB'].isna()))]
 
# TESTING VISUAL 2

print(df_ptd_cerrado_anterior2[df_ptd_cerrado_anterior2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado_anterior2[df_ptd_cerrado_anterior2["CODIGO_PROYECTO"] == "P-1704"].head(5)


# #### 4.8.4 - AGREGACIÓN COLUMNA MARGEN

# In[356]:


#CREACIÓN DE MARGENES

df_ptd_cerrado_anterior3 = df_ptd_cerrado_anterior2.copy()


# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_ptd_cerrado_anterior3.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_ptd_cerrado_anterior3 : ", df_ptd_cerrado_anterior3.shape)

df_ptd_cerrado_anterior3 = pd.merge(df_ptd_cerrado_anterior3, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado_anterior3 : ", df_ptd_cerrado_anterior3.shape)
df_ptd_cerrado_anterior3.sample(5)


# In[357]:


# TESTING VISUAL 1

print(df_ptd_cerrado_anterior3[df_ptd_cerrado_anterior3["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado_anterior3[df_ptd_cerrado_anterior3["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[358]:


# TESTING VISUAL 2

print(df_ptd_cerrado_anterior3[df_ptd_cerrado_anterior3["CODIGO_PROYECTO"] == "P-1727"]["TOTAL"].sum())
df_ptd_cerrado_anterior3[df_ptd_cerrado_anterior3["CODIGO_PROYECTO"] == "P-1704"].head(5)


# In[359]:


df_ptd_cerrado_anterior3.to_csv('archivos_respaldo/df_ptd_cerrado_anterior3.csv', index = False)


# In[ ]:





# ### 4.9 - MERGE PTD + MES EN CURSO (PROYECTADO)
# Cruce entre df_ptd_cerrado3 + mes_en_curso_proy5
# 
# NOTA IMPORTANTE:
# Ambos dataframes vienen depurados de los MERGES anteriores y no es necesario trabajar con el df_libro_mayor5_base2, por lo tanto solo se realiza concatenación y se crean las filas 1. TOTAL y el MARGEN. 

# #### 4.9.1 - EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[360]:


# TRATAMIENTO DATAFRAME df_ptd_cerrado3_1

# Se realiza una copia del dataframe 
df_ptd_cerrado3_1 = df_ptd_cerrado3.copy()

# Se Seleccionan columnas utiles:

df_ptd_cerrado3_1 = df_ptd_cerrado3_1[["CODIGO_PROYECTO", "TIPO_CUENTA", "NOMBRE_OBRA", "NOMBRE_CLIENTE", "TOTAL"]]

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME  : df_ptd_cerrado3   : ", df_ptd_cerrado3.shape)
print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_ptd_cerrado3_1 : ", df_ptd_cerrado3_1.shape)

# Se renombra campo "TOTAL"
df_ptd_cerrado3_1 = df_ptd_cerrado3_1.rename(columns={"TOTAL": "TOTAL PTD"})

df_ptd_cerrado3_1.sample(5)


# In[361]:


# TRATAMIENTO DATAFRAME df_ptd_cerrado3_1

# Se realiza una copia del dataframe 
mes_en_curso_proy5_1 = mes_en_curso_proy5.copy()

# Se Seleccionan columnas utiles:

mes_en_curso_proy5_1 = mes_en_curso_proy5_1[["CODIGO_PROYECTO", "TIPO_CUENTA", "TOTAL"]]

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME  : mes_en_curso_proy5  : ", mes_en_curso_proy5.shape)
print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_proy5_1 : ", mes_en_curso_proy5_1.shape)

# Se renombra campo "TOTAL"
mes_en_curso_proy5_1 = mes_en_curso_proy5_1.rename(columns={"TOTAL": "TOTAL MEC PROY"})

mes_en_curso_proy5_1.sample(5)


# #### 4.9.2 - MERGE DE DATAFRAMES 

# In[362]:


# Se hace merge manteniendo como base df_ptd_cerrado3_1 que viene del total de proyectos existentes en el libro mayor 2023

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado3_1 : ", df_ptd_cerrado3_1.shape)

df_ptd_cerrado_y_proyectado = pd.merge(df_ptd_cerrado3_1, mes_en_curso_proy5_1, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado : ", df_ptd_cerrado_y_proyectado.shape)

df_ptd_cerrado_y_proyectado.sample(5)


# In[363]:


# Se estandarizan columnas de Totales y se agrega columna TOTAL 

# Reemplazar NaN por cero en las columnas "TOTAL YTD" y "TOTAL LB OLD"
df_ptd_cerrado_y_proyectado["TOTAL PTD"] = df_ptd_cerrado_y_proyectado["TOTAL PTD"].fillna(0)
df_ptd_cerrado_y_proyectado["TOTAL MEC PROY"] = df_ptd_cerrado_y_proyectado["TOTAL MEC PROY"].fillna(0)

# Crear la nueva columna "TOTAL" que suma "TOTAL YTD" y "TOTAL LB OLD"
df_ptd_cerrado_y_proyectado["TOTAL"] = df_ptd_cerrado_y_proyectado["TOTAL PTD"] + df_ptd_cerrado_y_proyectado["TOTAL MEC PROY"]
df_ptd_cerrado_y_proyectado.sample(5)


# In[364]:


# TESTING VISUAL 1

print(df_ptd_cerrado_y_proyectado[df_ptd_cerrado_y_proyectado["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado_y_proyectado[df_ptd_cerrado_y_proyectado["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[365]:


# TESTING VISUAL 2

print(df_ptd_cerrado_y_proyectado[df_ptd_cerrado_y_proyectado["CODIGO_PROYECTO"] == "P-1727"]["TOTAL"].sum())
df_ptd_cerrado_y_proyectado[df_ptd_cerrado_y_proyectado["CODIGO_PROYECTO"] == "P-1727"].head(5)


# #### 4.9.3 - AGREGACIÓN COLUMNA MARGEN

# In[366]:


#CREACIÓN DE MARGENES

df_ptd_cerrado_y_proyectado2 = df_ptd_cerrado_y_proyectado.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_ptd_cerrado_y_proyectado2.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado2 : ", df_ptd_cerrado_y_proyectado2.shape)

df_ptd_cerrado_y_proyectado2 = pd.merge(df_ptd_cerrado_y_proyectado2, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado2 : ", df_ptd_cerrado_y_proyectado2.shape)
df_ptd_cerrado_y_proyectado2.sample(10)


# In[367]:


# TESTING VISUAL 1

print(df_ptd_cerrado_y_proyectado2[df_ptd_cerrado_y_proyectado2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado_y_proyectado2[df_ptd_cerrado_y_proyectado2["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[368]:


# TESTING VISUAL 2

print(df_ptd_cerrado_y_proyectado2[df_ptd_cerrado_y_proyectado2["CODIGO_PROYECTO"] == "P-1727"]["TOTAL"].sum())
df_ptd_cerrado_y_proyectado2[df_ptd_cerrado_y_proyectado2["CODIGO_PROYECTO"] == "P-1727"].head(5)


# In[369]:


df_ptd_cerrado_y_proyectado2.to_csv('archivos_respaldo/df_ptd_cerrado_y_proyectado2.csv', index = False)


# In[ ]:





# ### 4.10 - MERGE PTD + MES EN CURSO (PROYECTADO) (PERSPECTIVA MES ANTERIOR)
# Cruce entre df_ptd_cerrado_anterior3 + mes_en_curso_proy_2M_5
# 
# NOTA IMPORTANTE:
# Ambos dataframes vienen depurados de los MERGES anteriores y no es necesario trabajar con el df_libro_mayor5_base2, por lo tanto solo se realiza concatenación y se crean las filas 1. TOTAL y el MARGEN. 

# #### 4.10.1 - EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[370]:


# TRATAMIENTO DATAFRAME df_ptd_cerrado3_1

# Se realiza una copia del dataframe 
df_ptd_cerrado_anterior3_1 = df_ptd_cerrado_anterior3.copy()

# Se Seleccionan columnas utiles:

df_ptd_cerrado_anterior3_1 = df_ptd_cerrado_anterior3_1[["CODIGO_PROYECTO", "TIPO_CUENTA", "NOMBRE_OBRA", "NOMBRE_CLIENTE", "TOTAL"]]

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME  : df_ptd_cerrado_anterior3   : ", df_ptd_cerrado_anterior3.shape)
print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: df_ptd_cerrado_anterior3_1 : ", df_ptd_cerrado_anterior3_1.shape)

# Se renombra campo "TOTAL"
df_ptd_cerrado_anterior3_1 = df_ptd_cerrado_anterior3_1.rename(columns={"TOTAL": "TOTAL PTD"})

df_ptd_cerrado_anterior3_1.sample(5)


# In[371]:


# TRATAMIENTO DATAFRAME mes en curso proyectado

# Se realiza una copia del dataframe 
mes_en_curso_proy_2M_5_1 = mes_en_curso_proy_2M_5.copy()

# Se Seleccionan columnas utiles:

mes_en_curso_proy_2M_5_1 = mes_en_curso_proy_2M_5_1[["CODIGO_PROYECTO", "TIPO_CUENTA", "TOTAL"]]

print("DIMENSIONES ANTES DE TRANSFORMACIÓN DATAFRAME  : mes_en_curso_proy_2M_5   : ", mes_en_curso_proy_2M_5.shape)
print("DIMENSIONES DESPUÉS DE TRANSFORMACIÓN DATAFRAME: mes_en_curso_proy_2M_5_1 : ", mes_en_curso_proy_2M_5_1.shape)

# Se renombra campo "TOTAL"
mes_en_curso_proy_2M_5_1 = mes_en_curso_proy_2M_5_1.rename(columns={"TOTAL": "TOTAL MEC PROY"})

mes_en_curso_proy_2M_5_1.sample(5)


# #### 4.10.2 - MERGE DE DATAFRAMES 

# In[372]:


# Se hace merge manteniendo como base df_ptd_cerrado3_1 que viene del total de proyectos existentes en el libro mayor 2023

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado_anterior3_1 : ", df_ptd_cerrado_anterior3_1.shape)

df_ptd_cerrado_y_proyectado_ant = pd.merge(df_ptd_cerrado_anterior3_1, mes_en_curso_proy_2M_5_1, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado_ant : ", df_ptd_cerrado_y_proyectado_ant.shape)

df_ptd_cerrado_y_proyectado_ant.sample(5)


# In[373]:


# Se estandarizan columnas de Totales y se agrega columna TOTAL 

# Reemplazar NaN por cero en las columnas "TOTAL YTD" y "TOTAL LB OLD"
df_ptd_cerrado_y_proyectado_ant["TOTAL PTD"] = df_ptd_cerrado_y_proyectado_ant["TOTAL PTD"].fillna(0)
df_ptd_cerrado_y_proyectado_ant["TOTAL MEC PROY"] = df_ptd_cerrado_y_proyectado_ant["TOTAL MEC PROY"].fillna(0)

# Crear la nueva columna "TOTAL" que suma "TOTAL YTD" y "TOTAL LB OLD"
df_ptd_cerrado_y_proyectado_ant["TOTAL"] = df_ptd_cerrado_y_proyectado_ant["TOTAL PTD"] + df_ptd_cerrado_y_proyectado_ant["TOTAL MEC PROY"]
df_ptd_cerrado_y_proyectado_ant.sample(5)


# In[374]:


# TESTING VISUAL 1

print(df_ptd_cerrado_y_proyectado_ant[df_ptd_cerrado_y_proyectado_ant["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado_y_proyectado_ant[df_ptd_cerrado_y_proyectado_ant["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[375]:


# TESTING VISUAL 2

print(df_ptd_cerrado_y_proyectado_ant[df_ptd_cerrado_y_proyectado_ant["CODIGO_PROYECTO"] == "P-1727"]["TOTAL"].sum())
df_ptd_cerrado_y_proyectado_ant[df_ptd_cerrado_y_proyectado_ant["CODIGO_PROYECTO"] == "P-1727"].head(5)


# #### 4.10.3 - AGREGACIÓN COLUMNA MARGEN

# In[376]:


#CREACIÓN DE MARGENES

df_ptd_cerrado_y_proyectado_ant2 = df_ptd_cerrado_y_proyectado_ant.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_ptd_cerrado_y_proyectado_ant2.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado_ant2 : ", df_ptd_cerrado_y_proyectado_ant2.shape)

df_ptd_cerrado_y_proyectado_ant2 = pd.merge(df_ptd_cerrado_y_proyectado_ant2, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado_ant2 : ", df_ptd_cerrado_y_proyectado_ant2.shape)
df_ptd_cerrado_y_proyectado_ant2.sample(10)


# In[377]:


# TESTING VISUAL 1

print(df_ptd_cerrado_y_proyectado_ant2[df_ptd_cerrado_y_proyectado_ant2["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_ptd_cerrado_y_proyectado_ant2[df_ptd_cerrado_y_proyectado_ant2["CODIGO_PROYECTO"] == "1. TOTAL"].head(5)


# In[378]:


# TESTING VISUAL 2

print(df_ptd_cerrado_y_proyectado_ant[df_ptd_cerrado_y_proyectado_ant["CODIGO_PROYECTO"] == "P-1704"]["TOTAL"].sum())
df_ptd_cerrado_y_proyectado_ant[df_ptd_cerrado_y_proyectado_ant["CODIGO_PROYECTO"] == "P-1704"].head(5)


# In[379]:


df_ptd_cerrado_y_proyectado_ant.to_csv('archivos_respaldo/df_ptd_cerrado_y_proyectado_ant.csv', index = False)


# In[ ]:





# ### 4.11 MERGE PRESUPUESTO
# Se realiza mergen entre los datos que provienen de la planilla de presupuesto y tabla de presupuestos.

# #### 4.11.1 CREACIÓN Y TRATAMIENTO INICIAL DE DATAFRAMES A CONCANTENAR.

# In[380]:


print("DIMENSIONES DATAFRAME *df_tabla_presupuesto3* :", df_tabla_presupuesto3.shape)
df_tabla_presupuesto4 = df_tabla_presupuesto3.copy()
print("DIMENSIONES DATAFRAME *df_presupuesto2* :", df_presupuesto2.shape)
df_presupuesto3 = df_presupuesto2.copy()


# In[381]:


df_tabla_presupuesto4 = df_tabla_presupuesto4[['CODIGO_PROYECTO', 'TIPO_COSTO', 'TOTAL', 'ORIGEN']]
df_tabla_presupuesto4.rename(columns={'TIPO_COSTO': 'TIPO_CUENTA'}, inplace=True)

df_tabla_presupuesto4.sample(10)


# In[382]:


df_presupuesto3.rename(columns={'VALOR': 'TOTAL'}, inplace=True)
df_presupuesto3.sample(10)


# #### 4.11.2 SE CONCATENA LOS DATAFRAMES

# In[383]:


# Imprimir las dimensiones de los DataFrames
print("Dimensiones de df_tabla_presupuesto4:", df_tabla_presupuesto4.shape)
print("Dimensiones de df_presupuesto3:", df_presupuesto3.shape)

# Concatenar los DataFrames
df_presupuesto_final = pd.concat([df_tabla_presupuesto4, df_presupuesto3], ignore_index=True)
print("Dimensiones de df_presupuesto_final:", df_presupuesto_final.shape)

df_presupuesto_final.sample(10)


# #### 4.11.3 SE REALIZA MERGE CON CODIGOS DE PROYECTO

# In[384]:


# Se hace merge con los codigos de proyecto.

print("Dimensiones de df_libro_mayor5_base2", df_libro_mayor5_base2.shape)

df_presupuesto_final2 = pd.merge(df_libro_mayor5_base2, df_presupuesto_final, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("Dimensiones de df_presupuesto_final2", df_presupuesto_final2.shape)
df_presupuesto_final2.sample(10)


# #### 4.11.4 SE AGREGAN FILAS DE "1.TOTAL"

# In[385]:


# Calcular la suma de los valores totales para cada tipo de cuenta


df_total = df_presupuesto_final2.groupby('TIPO_CUENTA')['TOTAL'].sum().reset_index()
df_total['CODIGO_PROYECTO'] = '1. TOTAL'

# Agregar las filas adicionales al DataFrame
df_presupuesto_final2 = pd.concat([df_presupuesto_final2, df_total], ignore_index=True)

df_presupuesto_final2.sample(10)


# In[386]:


# Modificar las columnas "NOMBRE_OBRA" y "NOMBRE_CLIENTE" para "1. TOTAL"
df_presupuesto_final2.loc[df_presupuesto_final2['CODIGO_PROYECTO'] == '1. TOTAL', ['NOMBRE_OBRA', 'NOMBRE_CLIENTE']] = '1. TOTAL'

df_presupuesto_final2.sample(10)      


# #### 4.11.5 AGREGACIÓN COLUMNA MARGEN

# In[387]:


#CREACIÓN DE MARGENES

df_presupuesto_final3 = df_presupuesto_final2.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_presupuesto_final3.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_presupuesto_final3 : ", df_presupuesto_final3.shape)

df_presupuesto_final4 = pd.merge(df_presupuesto_final3, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_presupuesto_final4 : ", df_presupuesto_final4.shape)
df_presupuesto_final4.sample(10)


# In[388]:


# TESTING VISUAL 1

print(df_presupuesto_final4[df_presupuesto_final4["CODIGO_PROYECTO"] == "1. TOTAL"]["TOTAL"].sum())
df_presupuesto_final4 = df_presupuesto_final4[~((df_presupuesto_final4['CODIGO_PROYECTO'] == '1. TOTAL') & df_presupuesto_final4['TOTAL'].isna())]
df_presupuesto_final4[df_presupuesto_final4["CODIGO_PROYECTO"] == "1. TOTAL"]


# In[389]:


# TESTING VISUAL 2

print(df_presupuesto_final4[df_presupuesto_final4["CODIGO_PROYECTO"] == "P-1704"]["TOTAL"].sum())
df_presupuesto_final4 = df_presupuesto_final4[(df_presupuesto_final4['CODIGO_PROYECTO'] != '1. TOTAL') | (df_presupuesto_final4['ORIGEN'] != 'AGREGACIÓN TIPO_CUENTA VALOR O')]
df_presupuesto_final4[df_presupuesto_final4["CODIGO_PROYECTO"] == "P-1704"]


# In[390]:


df_presupuesto_final4.to_csv('archivos_respaldo/df_presupuesto_final4.csv', index = False)


# In[ ]:





# ### 4.12 MERGE PENDIENTE (PRESUPUESTO -PDT CERRADO)

# #### 4.12.1 EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[391]:


# Exploración de dataframe base "df_libro_mayor5_base2"

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME  : df_libro_mayor5_base2 : ", df_libro_mayor5_base2.shape)
df_libro_mayor5_base2.sample(5)


# In[392]:


# Exploración y tratamiento de dataframe de presupuesto "df_presupuesto_final4"

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME  : df_presupuesto_final4 : ", df_presupuesto_final4.shape)

df_presupuesto_final4_1 = df_presupuesto_final4.copy()

df_presupuesto_final4_1 = df_presupuesto_final4_1.pivot_table(values="TOTAL", index=['CODIGO_PROYECTO', 'TIPO_CUENTA'], aggfunc='sum')
df_presupuesto_final4_1 = pd.DataFrame(df_presupuesto_final4_1.to_records())

df_presupuesto_final4_1.rename(columns={'TOTAL': 'TOTAL_PREP'}, inplace=True)

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME  : df_presupuesto_final4_1 : ", df_presupuesto_final4_1.shape)

df_presupuesto_final4_1.sample(10)


# In[393]:


# Exploración y tratamiento de dataframe de presupuesto "df_ptd_cerrado3"

# Se Crea una copia del dataframe df_ptd_cerrado3 para trabajarlo 

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME  : df_ptd_cerrado3 : ", df_ptd_cerrado3.shape)

df_ptd_cerrado3_1= df_ptd_cerrado3.drop(["NOMBRE_OBRA","NOMBRE_CLIENTE","TOTAL_LB","TOTAL YTD","TOTAL LB OLD","MARGEN"], axis=1)

df_ptd_cerrado3_2 = df_ptd_cerrado3_1.pivot_table(values="TOTAL", index=['CODIGO_PROYECTO', 'TIPO_CUENTA'], aggfunc='sum')
df_ptd_cerrado3_2 = pd.DataFrame(df_ptd_cerrado3_2.to_records())

print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado3_1 : ", df_ptd_cerrado3_1.shape)
df_ptd_cerrado3_2.rename(columns={'TOTAL': 'TOTAL_PDT'}, inplace=True)

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME  : df_ptd_cerrado3_2 : ", df_ptd_cerrado3_2.shape)

df_ptd_cerrado3_2.sample(10)


# #### 4.12.2 MERGE ENTRE DATAFRAMES 

# In[394]:


# MERGE df_libro_mayor5_2 y df_presupuesto_final5_2

print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_libro_mayor5_base2      : ", df_libro_mayor5_base2.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_presupuesto_final4_1    : ", df_presupuesto_final4_1.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado3_2          : ", df_ptd_cerrado3_2.shape)

df_pendiente = df_libro_mayor5_base2.merge(df_presupuesto_final4_1, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS De CAMBIOS DATAFRAME: df_pendiente               : ", df_pendiente.shape)

df_pendiente.sample(5)


# In[395]:


# MERGE df_pendiente y df_ptd_cerrado3_2

print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_pendiente               : ", df_pendiente.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado3_2          : ", df_ptd_cerrado3_2.shape)

df_pendiente2 = df_pendiente.merge(df_ptd_cerrado3_2, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS De CAMBIOS DATAFRAME: df_pendiente2              : ", df_pendiente2.shape)
df_pendiente2.sample(5)


# In[396]:


# TESTING VISUAL 1
 
df_pendiente2[df_pendiente2["CODIGO_PROYECTO"]=="P-1643"]


# In[397]:


# TESTING VISUAL 2
 
df_pendiente2[df_pendiente2["CODIGO_PROYECTO"]=="1. TOTAL"]


# #### 4.12.3 CALCULO DE COLUMNA TOTAL
# 
# El objetivo de este Dataframe es lograr identificar la diferencia entre el el presupuesto y el PDT Cerrado.

# In[398]:


# Modificar los valores negativos a positivos
df_pendiente2['TOTAL_PREP2'] = np.where(df_pendiente2['TOTAL_PREP'] < 0, df_pendiente2['TOTAL_PREP'] * -1, df_pendiente2['TOTAL_PREP'])

df_pendiente2['TOTAL_PDT2'] = np.where(df_pendiente2['TOTAL_PDT'] < 0, df_pendiente2['TOTAL_PDT'] * -1, df_pendiente2['TOTAL_PDT'])

# Calcular la columna "TOTAL" con los valores positivos
df_pendiente2['TOTAL_1'] = df_pendiente2['TOTAL_PREP2'] - df_pendiente2['TOTAL_PDT2']

df_pendiente2.sample(5)


# In[399]:


# TESTING VISUAL 1
 
df_pendiente2[df_pendiente2["CODIGO_PROYECTO"]=="P-1704"]


# In[400]:


# Se realiza estandarización de columna TOTAL considerando que los Tipos de cuenta de Costos deben estar en valor negativo.

# Crear nueva columna 'TOTAL' con el valor de 'TOTAL_PREV'
df_pendiente2['TOTAL'] = df_pendiente2['TOTAL_1']

# Aplicar condiciones para cambiar el valor a negativo
mask = (df_pendiente2['TIPO_CUENTA'].isin(['2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN'])) & (df_pendiente2['TOTAL_1'] != 0)
df_pendiente2.loc[mask, 'TOTAL'] *= -1

# Mantener el valor de 'TOTAL_PREV' como negativo si ya es negativo
df_pendiente2.loc[df_pendiente2['TOTAL_1'] < 0, 'TOTAL'] *= -1

df_pendiente2.sample(10)


# In[401]:


df_pendiente3 = df_pendiente2.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_pendiente3.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_pendiente3 : ", df_pendiente3.shape)

df_pendiente3 = pd.merge(df_pendiente3, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_pendiente3 : ", df_pendiente3.shape)
df_pendiente3.sample(5)


# In[402]:


# TESTING VISUAL 1
 
df_pendiente3[df_pendiente3["CODIGO_PROYECTO"]=="P-1727"]


# In[403]:


# TESTING VISUAL 2
 
df_pendiente3[df_pendiente3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[404]:


df_pendiente3.to_csv('archivos_respaldo/df_pendiente3.csv', index = False)


# In[ ]:





# ### 4.13 MERGE PENDIENTE (PRESUPUESTO -PDT CERRADO) (PERSPECTIVA MES ANTERIOR)

# #### 4.13.1 EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[405]:


# Exploración de dataframe base "df_libro_mayor5_base2"

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME  : df_libro_mayor5_base2 : ", df_libro_mayor5_base2.shape)
df_libro_mayor5_base2.sample(5)


# In[406]:


# Exploración y tratamiento de dataframe de presupuesto "df_presupuesto_final4"

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME  : df_presupuesto_final4 : ", df_presupuesto_final4.shape)

df_presupuesto_final4_1_1 = df_presupuesto_final4.copy()

df_presupuesto_final4_1_1 = df_presupuesto_final4_1_1.pivot_table(values="TOTAL", index=['CODIGO_PROYECTO', 'TIPO_CUENTA'], aggfunc='sum')
df_presupuesto_final4_1_1 = pd.DataFrame(df_presupuesto_final4_1_1.to_records())

df_presupuesto_final4_1_1.rename(columns={'TOTAL': 'TOTAL_PREP'}, inplace=True)

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME  : df_presupuesto_final4_1_1 : ", df_presupuesto_final4_1_1.shape)

df_presupuesto_final4_1_1.sample(10)


# In[407]:


# Exploración y tratamiento de dataframe de presupuesto "df_ptd_cerrado3"

# Se Crea una copia del dataframe df_ptd_cerrado3 para trabajarlo 

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME  : df_ptd_cerrado_anterior3 : ", df_ptd_cerrado_anterior3.shape)

df_ptd_cerrado3_1_1 = df_ptd_cerrado_anterior3.drop(["NOMBRE_OBRA","NOMBRE_CLIENTE","TOTAL_LB","TOTAL YTD","TOTAL LB OLD","MARGEN"], axis=1)

df_ptd_cerrado3_1_2 = df_ptd_cerrado3_1_1.pivot_table(values="TOTAL", index=['CODIGO_PROYECTO', 'TIPO_CUENTA'], aggfunc='sum')
df_ptd_cerrado3_1_2 = pd.DataFrame(df_ptd_cerrado3_1_2.to_records())

print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado3_1_2 : ", df_ptd_cerrado3_1_2.shape)
df_ptd_cerrado3_1_2.rename(columns={'TOTAL': 'TOTAL_PDT'}, inplace=True)

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME  : df_ptd_cerrado3_1_2 : ", df_ptd_cerrado3_1_2.shape)

df_ptd_cerrado3_1_2.sample(10)


# #### 4.13.2 MERGE ENTRE DATAFRAMES 

# In[408]:


# MERGE df_libro_mayor5_2 y df_presupuesto_final5_2

print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_libro_mayor5_base2      : ", df_libro_mayor5_base2.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_presupuesto_final4_1_1  : ", df_presupuesto_final4_1_1.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado3_1_2        : ", df_ptd_cerrado3_1_2.shape)

df_pendiente_2 = df_libro_mayor5_base2.merge(df_presupuesto_final4_1_1, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS De CAMBIOS DATAFRAME: df_pendiente_2             : ", df_pendiente_2.shape)

df_pendiente_2.sample(5)


# In[409]:


# MERGE df_pendiente y df_ptd_cerrado3_2

print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_pendiente_2             : ", df_pendiente_2.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado3_1_2        : ", df_ptd_cerrado3_1_2.shape)

df_pendiente_2 = df_pendiente_2.merge(df_ptd_cerrado3_1_2, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS De CAMBIOS DATAFRAME: df_pendiente_2              : ", df_pendiente_2.shape)
df_pendiente_2.sample(5)


# In[410]:


# TESTING VISUAL 1
 
df_pendiente_2[df_pendiente_2["CODIGO_PROYECTO"]=="P-1643"]


# #### 4.13.3 CALCULO DE COLUMNA TOTAL
# 
# El objetivo de este Dataframe es lograr identificar la diferencia entre el el presupuesto y el PDT Cerrado.

# In[411]:


# Modificar los valores negativos a positivos
df_pendiente_2['TOTAL_PREP2'] = np.where(df_pendiente_2['TOTAL_PREP'] < 0, df_pendiente_2['TOTAL_PREP'] * -1, df_pendiente_2['TOTAL_PREP'])

df_pendiente_2['TOTAL_PDT2'] = np.where(df_pendiente_2['TOTAL_PDT'] < 0, df_pendiente_2['TOTAL_PDT'] * -1, df_pendiente_2['TOTAL_PDT'])

# Calcular la columna "TOTAL" con los valores positivos
df_pendiente_2['TOTAL_1'] = df_pendiente_2['TOTAL_PREP2'] - df_pendiente_2['TOTAL_PDT2']

df_pendiente_2.sample(5)


# In[412]:


# TESTING VISUAL 1
 
df_pendiente_2[df_pendiente_2["CODIGO_PROYECTO"]=="P-1704"]


# In[413]:


# Se realiza estandarización de columna TOTAL considerando que los Tipos de cuenta de Costos deben estar en valor negativo.

# Crear nueva columna 'TOTAL' con el valor de 'TOTAL_PREV'
df_pendiente_2['TOTAL'] = df_pendiente_2['TOTAL_1']

# Aplicar condiciones para cambiar el valor a negativo
mask = (df_pendiente_2['TIPO_CUENTA'].isin(['2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN'])) & (df_pendiente_2['TOTAL_1'] != 0)
df_pendiente_2.loc[mask, 'TOTAL'] *= -1

# Mantener el valor de 'TOTAL_PREV' como negativo si ya es negativo
df_pendiente_2.loc[df_pendiente_2['TOTAL_1'] < 0, 'TOTAL'] *= -1

df_pendiente_2.sample(10)


# In[414]:


df_pendiente_3 = df_pendiente_2.copy()

# Esta línea de código es para evitar ver el error.
with np.errstate(divide='ignore', invalid='ignore'):

    df_margen = df_pendiente_3.groupby(['CODIGO_PROYECTO']).apply(lambda x: pd.Series({
        'MARGEN': x.loc[x['TIPO_CUENTA'].isin(['1. INGRESO','2. COSTO MATERIALES', '3. COSTO MANO DE OBRA', '4. COSTO SUPERVISIÓN']), 'TOTAL'].sum() / x.loc[x['TIPO_CUENTA'] == '1. INGRESO', 'TOTAL'].sum()
    }))

df_margen = pd.DataFrame(df_margen.to_records())
df_margen['MARGEN'] = df_margen['MARGEN'].fillna(0).replace(-np.inf, 0)
df_margen.replace([np.inf, -np.inf, np.nan], 0, inplace=True)


# mostrar el DataFrame resultante
df_margen.sample(10)


print("DIMENSIONES ANTES   DE CAMBIOS DATAFRAME: df_pendiente_3 : ", df_pendiente_3.shape)

df_pendiente_3 = pd.merge(df_pendiente_3, df_margen, on=['CODIGO_PROYECTO'], how='left')

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_pendiente_3 : ", df_pendiente_3.shape)
df_pendiente_3.sample(5)


# In[415]:


# TESTING VISUAL 1
 
df_pendiente_3[df_pendiente_3["CODIGO_PROYECTO"]=="P-1727"]


# In[416]:


# TESTING VISUAL 2
 
df_pendiente_3[df_pendiente_3["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[417]:


df_pendiente_3.to_csv('archivos_respaldo/df_pendiente_3.csv', index = False)


# In[ ]:





# ### 4.14 MERGE PDT CERRADO VS PRESUPUESTO

# #### 4.14.1 EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[418]:


# Exploración de dataframe df_pdt_cerrado

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado3 : ", df_ptd_cerrado3.shape)

df_ptd_cerrado3_2 = df_ptd_cerrado3.copy()

df_ptd_cerrado3_2.rename(columns={'TOTAL': 'TOTAL_PDT'}, inplace=True)
df_ptd_cerrado3_2.sample(5)


# In[419]:


# Exploración de dataframe presupuesto
df_presupuesto_final4.sample(10)

df_presupuesto_final4_1 = df_presupuesto_final4.copy()
df_presupuesto_final4_1.rename(columns={'TOTAL': 'TOTAL_PREP'}, inplace=True)

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_presupuesto_final4 : ", df_presupuesto_final4.shape)

df_presupuesto_final4_2 = pd.pivot_table(df_presupuesto_final4_1, values=['TOTAL_PREP'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum', fill_value=0)
df_presupuesto_final4_2 = pd.DataFrame(df_presupuesto_final4_2.to_records())

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_presupuesto_final4_2 : ", df_presupuesto_final4_2.shape)

df_presupuesto_final4_2.sample(5)


# #### 4.14.2 MERGE ENTRE DATAFRAMES

# In[420]:


print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado3_2                  : ", df_ptd_cerrado3_2.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_presupuesto_final4_2            : ", df_presupuesto_final4_2.shape)

df_pdt_vs_prep = df_ptd_cerrado3_2.merge(df_presupuesto_final4_2, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS De CAMBIOS DATAFRAME: df_pdt_vs_prep           : ", df_pdt_vs_prep.shape)

df_pdt_vs_prep.sample(5)


# #### 4.14.3 CREACIÓN DE COLUMNA % DE AVANCE

# In[421]:


df_pdt_vs_prep['% AVANCE'] = df_pdt_vs_prep['TOTAL_PDT'] / df_pdt_vs_prep['TOTAL_PREP']

# Reemplazar NaN por cero
df_pdt_vs_prep['% AVANCE'] = df_pdt_vs_prep['% AVANCE'].fillna(0)

# Reemplazar -inf por cero
df_pdt_vs_prep['% AVANCE'].replace(-np.inf, 0, inplace=True)

# Reemplazar inf por cero
df_pdt_vs_prep['% AVANCE'] = df_pdt_vs_prep['% AVANCE'].replace(np.inf, 0)

df_pdt_vs_prep.head(10)


# In[422]:


# TESTING VISUAL 1
 
df_pdt_vs_prep[df_pdt_vs_prep["CODIGO_PROYECTO"]=="P-1727"]


# In[423]:


# TESTING VISUAL 2
 
df_pdt_vs_prep[df_pdt_vs_prep["CODIGO_PROYECTO"]=="1. TOTAL"]


# In[424]:


df_pdt_vs_prep.to_csv('archivos_respaldo/df_pdt_vs_prep.csv', index = False)


# In[ ]:





# ### 4.15 MERGE PDT CERRADO VS PRESUPUESTO (PERSPECTIVA MES ANTERIOR)

# #### 4.15.1 EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[425]:


# Exploración de dataframe df_pdt_cerrado

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado3 : ", df_ptd_cerrado3.shape)

df_ptd_cerrado3_2_2 = df_ptd_cerrado_anterior3.copy()

df_ptd_cerrado3_2_2.rename(columns={'TOTAL': 'TOTAL_PDT'}, inplace=True)
df_ptd_cerrado3_2_2.sample(5)


# In[426]:


# Exploración presupuesto, creado en el punto anterior y que se reutiliza en éste.

df_presupuesto_final4_2.sample(5)


# #### 4.15.2 MERGE ENTRE DATAFRAMES

# In[427]:


print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado3_2_                 : ", df_ptd_cerrado3_2_2.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_presupuesto_final4_2            : ", df_presupuesto_final4_2.shape)

df_pdt_vs_prep_2 = df_ptd_cerrado3_2_2.merge(df_presupuesto_final4_2, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS De CAMBIOS DATAFRAME: df_pdt_vs_prep_2           : ", df_pdt_vs_prep_2.shape)

df_pdt_vs_prep_2.sample(5)


# #### 4.15.3 CREACIÓN DE COLUMNA % DE AVANCE

# In[430]:


df_pdt_vs_prep_2['% AVANCE'] = df_pdt_vs_prep_2['TOTAL_PDT'] / df_pdt_vs_prep_2['TOTAL_PREP']

# Reemplazar NaN por cero
df_pdt_vs_prep_2['% AVANCE'] = df_pdt_vs_prep_2['% AVANCE'].fillna(0)

# Reemplazar -inf por cero
df_pdt_vs_prep_2['% AVANCE'].replace(-np.inf, 0, inplace=True)

# Reemplazar inf por cero
df_pdt_vs_prep_2['% AVANCE'] = df_pdt_vs_prep_2['% AVANCE'].replace(np.inf, 0)

df_pdt_vs_prep_2.head(10)


# In[431]:


# TESTING VISUAL 1
 
df_pdt_vs_prep_2[df_pdt_vs_prep_2["CODIGO_PROYECTO"]=="P-1727"]


# In[432]:


# TESTING VISUAL 2
 
df_pdt_vs_prep_2[df_pdt_vs_prep_2["CODIGO_PROYECTO"]=="P-1704"]


# In[433]:


df_pdt_vs_prep_2.to_csv('archivos_respaldo/df_pdt_vs_prep_2.csv', index = False)


# In[ ]:





# ### 4.16 MERGE PTD CERRADO + PROYECTADO VS PRESUPUESTO

# #### 4.16.1 EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[434]:


# Exploración de dataframe df_ptd_cerrado_y_proyectado2

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado2 : ", df_ptd_cerrado_y_proyectado2.shape)

df_ptd_cerrado_y_proyectado2_2 = df_ptd_cerrado_y_proyectado2.copy()

df_ptd_cerrado_y_proyectado2_2.rename(columns={'TOTAL': 'TOTAL_PDT'}, inplace=True)
df_ptd_cerrado_y_proyectado2_2.sample(5)


# In[435]:


# Exploración de dataframe presupuesto

df_presupuesto_final4_2 = df_presupuesto_final4.copy()
df_presupuesto_final4_2.rename(columns={'TOTAL': 'TOTAL_PDT_PREP'}, inplace=True)

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_presupuesto_final4_2 : ", df_presupuesto_final4_2.shape)

df_presupuesto_final4_2 = pd.pivot_table(df_presupuesto_final4_2, values=['TOTAL_PDT_PREP'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum', fill_value=0)
df_presupuesto_final4_2 = pd.DataFrame(df_presupuesto_final4_2.to_records())

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_presupuesto_final4_2 : ", df_presupuesto_final4_2.shape)

df_presupuesto_final4_2.sample(5)


# #### 4.16.2 MERGE ENTRE DATAFRAMES

# In[436]:


print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado2_2 : ", df_ptd_cerrado_y_proyectado2_2.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_presupuesto_final4_2        : ", df_presupuesto_final4_2.shape)

df_pdt_proy_vs_prep = df_ptd_cerrado_y_proyectado2_2.merge(df_presupuesto_final4_2, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS De CAMBIOS DATAFRAME: df_pdt_proy_vs_prep           : ", df_pdt_proy_vs_prep.shape)

df_pdt_proy_vs_prep.sample(5)


# #### 4.16.3 CREACIÓN DE COLUMNA % DE AVANCE

# In[437]:


df_pdt_proy_vs_prep['% AVANCE'] = df_pdt_proy_vs_prep['TOTAL_PDT'] / df_pdt_proy_vs_prep['TOTAL_PDT_PREP']

# Reemplazar NaN por cero
df_pdt_proy_vs_prep['% AVANCE'] = df_pdt_proy_vs_prep['% AVANCE'].fillna(0)

# Reemplazar -inf por cero
df_pdt_proy_vs_prep['% AVANCE'].replace(-np.inf, 0, inplace=True)

# Reemplazar inf por cero
df_pdt_proy_vs_prep['% AVANCE'] = df_pdt_proy_vs_prep['% AVANCE'].replace(np.inf, 0)

df_pdt_proy_vs_prep.head(10)


# In[438]:


# TESTING VISUAL 1
 
df_pdt_proy_vs_prep[df_pdt_proy_vs_prep["CODIGO_PROYECTO"]=="P-1704"]


# In[439]:


# TESTING VISUAL 2
 
df_pdt_proy_vs_prep[df_pdt_proy_vs_prep["CODIGO_PROYECTO"]=="P-1704"]


# In[440]:


df_pdt_proy_vs_prep.to_csv('archivos_respaldo/df_pdt_proy_vs_prep.csv', index = False)


# In[ ]:





# ### 4.17 MERGE PTD CERRADO + PROYECTADO VS PRESUPUESTO (PERSPECTIVA MES ANTERIOR)

# #### 4.17.1 EXPLORACIÓN Y PREPARACIÓN DE DATAFRAMES

# In[441]:


# Exploración de dataframe df_ptd_cerrado_y_proyectado_ant2

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado_ant2 : ", df_ptd_cerrado_y_proyectado_ant2.shape)

df_ptd_cerrado_y_proyectado_ant2_2 = df_ptd_cerrado_y_proyectado_ant2.copy()

df_ptd_cerrado_y_proyectado_ant2_2.rename(columns={'TOTAL': 'TOTAL_PDT'}, inplace=True)
df_ptd_cerrado_y_proyectado_ant2_2.sample(5)


# In[442]:


# Exploración de dataframe presupuesto

df_presupuesto_final4_2_1 = df_presupuesto_final4.copy()
df_presupuesto_final4_2_1.rename(columns={'TOTAL': 'TOTAL_PDT_PREP'}, inplace=True)

print("DIMENSIONES ANTES DE CAMBIOS DATAFRAME: df_presupuesto_final4_2 : ", df_presupuesto_final4_2.shape)

df_presupuesto_final4_2_1 = pd.pivot_table(df_presupuesto_final4_2_1, values=['TOTAL_PDT_PREP'], index=['CODIGO_PROYECTO','TIPO_CUENTA'], aggfunc='sum', fill_value=0)
df_presupuesto_final4_2_1 = pd.DataFrame(df_presupuesto_final4_2_1.to_records())

print("DIMENSIONES DESPUÉS DE CAMBIOS DATAFRAME: df_presupuesto_final4_2_1 : ", df_presupuesto_final4_2_1.shape)

df_presupuesto_final4_2_1.sample(5)


# #### 4.17.2 MERGE ENTRE DATAFRAMES

# In[443]:


print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_ptd_cerrado_y_proyectado_ant2_2 : ", df_ptd_cerrado_y_proyectado_ant2_2.shape)
print("DIMENSIONES ANTERIOR A CAMBIOS DATAFRAME: df_presupuesto_final4_2_1          : ", df_presupuesto_final4_2_1.shape)

df_pdt_proy_vs_prep_2 = df_ptd_cerrado_y_proyectado_ant2_2.merge(df_presupuesto_final4_2_1, on=['CODIGO_PROYECTO','TIPO_CUENTA'], how='left')

print("DIMENSIONES DESPUÉS De CAMBIOS DATAFRAME: df_pdt_proy_vs_prep_2           : ", df_pdt_proy_vs_prep_2.shape)

df_pdt_proy_vs_prep_2.sample(5)


# #### 4.17.3 CREACIÓN DE COLUMNA % DE AVANCE

# In[444]:


df_pdt_proy_vs_prep_2['% AVANCE'] = df_pdt_proy_vs_prep_2['TOTAL_PDT'] / df_pdt_proy_vs_prep_2['TOTAL_PDT_PREP']

# Reemplazar NaN por cero
df_pdt_proy_vs_prep_2['% AVANCE'] = df_pdt_proy_vs_prep_2['% AVANCE'].fillna(0)

# Reemplazar -inf por cero
df_pdt_proy_vs_prep_2['% AVANCE'].replace(-np.inf, 0, inplace=True)

# Reemplazar inf por cero
df_pdt_proy_vs_prep_2['% AVANCE'] = df_pdt_proy_vs_prep_2['% AVANCE'].replace(np.inf, 0)

df_pdt_proy_vs_prep_2.head(10)


# In[445]:


# TESTING VISUAL 1
 
df_pdt_proy_vs_prep_2[df_pdt_proy_vs_prep_2["CODIGO_PROYECTO"]=="P-1704"]


# In[446]:


df_pdt_proy_vs_prep_2.to_csv('archivos_respaldo/df_pdt_proy_vs_prep_2.csv', index = False)


# In[ ]:





# In[ ]:





# ## 5. - EXPORTACIÓN DE ARCHIVOS

# In[447]:


# Conexión a google drive

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Credenciales de GOOGLE API, en archivo .json
credentials = ServiceAccountCredentials.from_json_keyfile_name('keen-extension-358919-9214486a06be.json', scope) # Your json file here

gc = gspread.authorize(credentials)

## SIEMPRE DAR ACCESO A ESTE USUARIO: test-321@keen-extension-358919.iam.gserviceaccount.com


# ### 5.1 EXPORTACIÓN LIBRO MAYOR PARA CUADRO FINANCIERO DE PROYECTOS

# In[448]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1COX0_p3dTPNLZMwoh__0uQdOYfP_AA1mw7lfKx4SMMQ')

# select a work sheet from its name
worksheet1 = gs.worksheet('Hoja 1')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe=df_libro_mayor6, include_index=False,
include_column_header=True, resize=True)


# ### 5.2 EXPORTACIÓN LIBRO MAYOR YTD HASTA MES CERRADO
# Dataframe: df_ytd_cerrado3

# In[449]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1_53Vj0j4xnqsWDdHDdetp3JmoUHRjLlvsUyi7tQXCY4')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_ytd_cerrado3, include_index=False,
include_column_header=True, resize=True)


# ### 5.2.1 EXPORTACIÓN LIBRO MAYOR YTD HASTA MES CERRADO (MES ANTERIOR) PERSPECTIVA MES ANTERIOR
# Dataframe: df_ytd_cerrado_2M_3

# In[450]:


gs = gc.open_by_key('1_53Vj0j4xnqsWDdHDdetp3JmoUHRjLlvsUyi7tQXCY4')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_ytd_cerrado_2M_3, include_index=False,
include_column_header=True, resize=True)


# ### 5.3 EXPORTACIÓN MES EN CURSO PROYECTADO
# Dataframe: mes_en_curso2

# In[451]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1xyeMVO6VL0yBCX6aZRcFxNKPH5yum2o2gF_HM2NSLIs')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= mes_en_curso_proy5, include_index=False,
include_column_header=True, resize=True)


# ### 5.3.1 EXPORTACIÓN MES EN CURSO PROYECTADO (MES ANTERIOR) PERSPECTIVA MES ANTERIOR
# Dataframe: mes_en_curso_2M

# In[452]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1xyeMVO6VL0yBCX6aZRcFxNKPH5yum2o2gF_HM2NSLIs')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= mes_en_curso_proy_2M_5, include_index=False,
include_column_header=True, resize=True)


# ### 5.4 EXPORTACIÓN MES EN CURSO

# In[453]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1k4Yf_ycqV1TjqPcS0eDGyUU_oKu9JVzYUHw9shUBGTM')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= mes_en_curso_real5, include_index=False,
include_column_header=True, resize=True)


# ### 5.4.1 EXPORTACIÓN MES EN CURSO PERSPECTIVA MES ANTERIOR

# In[454]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1k4Yf_ycqV1TjqPcS0eDGyUU_oKu9JVzYUHw9shUBGTM')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= mes_en_curso_real_2M_5, include_index=False,
include_column_header=True, resize=True)


# ### 5.5 EXPORTACIÓN YTD PROYECTADO

# In[455]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1_39cxdPhNrDcz2WJ-t3oLQRpgQPhWwFsopAGzcmxuuk')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_ytd_proyectado2, include_index=False,
include_column_header=True, resize=True)


# ### 5.5.1 EXPORTACIÓN YTD PROYECTADO PERSPECTIVA MES ANTERIOR

# In[456]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1_39cxdPhNrDcz2WJ-t3oLQRpgQPhWwFsopAGzcmxuuk')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_ytd_proyectado_2M_2, include_index=False,
include_column_header=True, resize=True)


# ### 5.6 EXPORTACIÓN PTD CERRADO

# In[457]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1bMRHlz-oMTZ7ccBXbEvjQ3es7mBcWxZqpVrPBXGAVjc')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_ptd_cerrado3, include_index=False,
include_column_header=True, resize=True)


# ### 5.6.1 EXPORTACIÓN PTD CERRADO (PERSPECTIVA MES ANTERIOR)

# In[458]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1bMRHlz-oMTZ7ccBXbEvjQ3es7mBcWxZqpVrPBXGAVjc')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_ptd_cerrado_anterior3, include_index=False,
include_column_header=True, resize=True)


# ### 5.7 EXPORTACIÓN PTD CERRADO + PROYECTADO

# In[459]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('14dw0WLmoa8gDJLcOkDJor17BCy7pozNQK7L1bSvJQqs')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_ptd_cerrado_y_proyectado2, include_index=False,
include_column_header=True, resize=True)


# ### 5.7.1 EXPORTACIÓN PTD CERRADO + PROYECTADO (PERSPECTIVA MES ANTERIOR)

# In[460]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('14dw0WLmoa8gDJLcOkDJor17BCy7pozNQK7L1bSvJQqs')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_ptd_cerrado_y_proyectado_ant2, include_index=False,
include_column_header=True, resize=True)


# ### 5.8 EXPORTACIÓN PRESUPUESTO

# In[461]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1yTtFi7x0rc_FU6xb-FrdQGKndttaf0dg3ENDyOO52eM')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_presupuesto_final4, include_index=False,
include_column_header=True, resize=True)


# ### 5.9 EXPORTACIÓN PENDIENTE

# In[462]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1qLDVshnNP-whjDaMYi1N4QSeeD6AK4EVSQtQx6Y438o')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_pendiente3, include_index=False,
include_column_header=True, resize=True)


# ### 5.10 EXPORTACIÓN PENDIENTE (PERSPECTIVA MES ANTERIOR)

# In[463]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1qLDVshnNP-whjDaMYi1N4QSeeD6AK4EVSQtQx6Y438o')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_pendiente_3, include_index=False,
include_column_header=True, resize=True)


# ### 5.11 EXPORTACIÓN PTD Cerrado vs Presupuesto

# In[464]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1ZsZGZ5uzyEK7rOqHXER0MYjKbrbiLK9cdeYlXk4t8oE')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_pdt_vs_prep, include_index=False,
include_column_header=True, resize=True)


# ### 5.12 EXPORTACIÓN PTD Cerrado vs Presupuesto (PERSPECTIVA MES ANTERIOR)

# In[465]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1ZsZGZ5uzyEK7rOqHXER0MYjKbrbiLK9cdeYlXk4t8oE')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_pdt_vs_prep_2, include_index=False,
include_column_header=True, resize=True)


# ### 5.13 EXPORTACIÓN  PTD Cerrado + Proyectado vs Presupuesto

# In[466]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1yqyEJ4mkcaS_kI7rrNZ8reRxqFhWdbhBtvDcSeWxkPo')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_actual')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_pdt_proy_vs_prep, include_index=False,
include_column_header=True, resize=True)


# ### 5.13 EXPORTACIÓN  PTD Cerrado + Proyectado vs Presupuesto (PERSPECTIVA ANTERIOR)

# In[467]:


# write to dataframe
# open a google sheet
gs = gc.open_by_key('1yqyEJ4mkcaS_kI7rrNZ8reRxqFhWdbhBtvDcSeWxkPo')

# select a work sheet from its name
worksheet1 = gs.worksheet('vista_anterior')
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe= df_pdt_proy_vs_prep_2, include_index=False,
include_column_header=True, resize=True)


# In[ ]:




