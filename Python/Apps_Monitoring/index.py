from kafka import KafkaConsumer
import pandas as pd
import json,time
import os
import datetime

from dash import Dash, html, dcc
import plotly.express as px
import warnings


warnings.simplefilter(action='ignore', category=FutureWarning)
# Initialize Kafka consumer
consumer = KafkaConsumer('belajar-IOT', bootstrap_servers=['192.168.0.5:9092']
                         ,auto_offset_reset='earliest'
                         , api_version=(0, 10))
df = pd.DataFrame()  # Initialize an empty list to store DataFrames
provinsi=input("Masukan Nama Provinsi :")



for message in consumer:
    os.system('cls')
    message_value = json.loads(message.value.decode('utf-8'))
    df = df.append(message_value, ignore_index=True)
    #df['time']=pd.to_datetime(df['time'])
    df['Jam']=pd.to_datetime(df['time']).dt.hour
    df=df[(df['regional']==provinsi)]
    df['tgl']=pd.to_datetime(df['time']).dt.date
    df=df[(df['tgl']==datetime.datetime.now().date())]
    df['RANK'] = df.groupby('regional')['time'].rank(ascending=False)

    df_result_last=df
    df_result_last=df_result_last[(df_result_last['RANK']==1.0)]
    
    df_result_analytic=df
    df_result_analytic=df_result_analytic.drop('time',axis=1)
    df_result_analytic=df_result_analytic.drop('RANK',axis=1)
    df_result_analytic=df_result_analytic.groupby(['name','Jam','regional']).mean().reset_index()
    df_result_analytic['cahaya']=df_result_analytic['cahaya'].apply(lambda x: round(x, 2))
    df_result_analytic['kelembaban']=df_result_analytic['kelembaban'].apply(lambda x: round(x, 2))
    df_result_analytic['temperature']=df_result_analytic['temperature'].apply(lambda x: round(x, 2))
    df_result_analytic['cahaya']=df_result_analytic['cahaya'].astype(str)+" %"
    df_result_analytic['kelembaban']=df_result_analytic['kelembaban'].astype(str)+" %"
    #df_grouped = df.groupby("nm_brng").size().reset_index(name="Total")
    print(" Suhu Di kota ",df_result_last['regional'].values[0], "Menunjukan Angka ",df_result_last['temperature'].values[0]
          ," C\n","dengan kelembabapan ",df_result_last['kelembaban'].values[0]," %\n",
          "dan intensitas cahaya ",df_result_last['cahaya'].values[0] ," %\n"
          ,"Pada Tanggal ",df_result_last['time'].values[0],"\n")
    print(" Berikut Adalah Tabel Suhu Rata Rata Per Jamnya")
    print(df_result_analytic)
 


