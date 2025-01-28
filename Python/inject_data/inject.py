from kafka import KafkaConsumer
import pandas as pd
import json,time
from dash import Dash, html, dcc
import plotly.express as px
import pyodbc

#koneksi
# Define the connection parameters
try:
    server = 'localhost'
    database = 'DB_Test'
    username = 'hary'
    password = '1234'
    # Create a connection string
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    # Establish a connection
    cnxn = pyodbc.connect(connection_string,autocommit=True)
    # Create a cursor object to interact with the database
    cursor = cnxn.cursor()
    print("Koneksi Berhasil")
except:
    print("Gagal Koneksi")
    
df=pd.read_excel("D:\Proyek\Implementasi_IOT_Padat_teknologi_kafka_untuk_analisa\data_cuaca_dari_jan_2024\merge_data_cuaca.xlsx")
print(df)
a=0
for index,row in df.iterrows():
        print("Jumlah Di insert= ",str(a),end="\r")
        cursor.execute("insert into Learn_IOT (name,temperature,kelembaban,cahaya,regional,time) \
                       values (?,?,?,?,?,?)", row['name'],row['temperature'], row['kelembaban'], row['cahaya'], row['regional'],row['time'])
        a=a+1