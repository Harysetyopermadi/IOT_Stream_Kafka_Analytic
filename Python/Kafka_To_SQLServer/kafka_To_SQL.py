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
# Initialize Kafka consumer
consumer = KafkaConsumer('belajar-IOT', bootstrap_servers=['192.168.0.5:9092']
                         #,auto_offset_reset='earliest'
                         , api_version=(0, 10))

df = pd.DataFrame()  # Initialize an empty list to store DataFrames

# Consume messages from Kafka topic

for message in consumer:
    message_value = json.loads(message.value.decode('utf-8'))
    df=pd.DataFrame.from_dict(message_value, orient='index')
    df=df.T.reset_index(drop=True)
    print(df)
    #df = df.append(message_value, ignore_index=True)
    for index,row in df.iterrows():
        cursor.execute("insert into Learn_IOT (name,temperature,kelembaban,cahaya,regional,time) \
                       values (?,?,?,?,?,?)", row['name'],row['temperature'], row['kelembaban'], row['cahaya'], row['regional'],row['time'])
    
    # df_grouped = df.groupby("nm_brng").size().reset_index(name="Total")
    # print(df_grouped,end="\r")


