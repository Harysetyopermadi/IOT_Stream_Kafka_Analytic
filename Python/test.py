from kafka import KafkaConsumer
import os
import pandas as pd
import json,time
from dash import Dash, html, dcc
import plotly.express as px
import uuid
# Initialize Kafka consumer
consumer = KafkaConsumer('belajar-IOT', bootstrap_servers=['192.168.0.5:9092']
                        ,auto_offset_reset='earliest',enable_auto_commit=True
                         , api_version=(0, 10))



df = pd.DataFrame()  # Initialize an empty list to store DataFrames

merge=pd.DataFrame()
for message in consumer:
    os.system('cls')
    message_value = json.loads(message.value.decode('utf-8'))
    df=pd.DataFrame.from_dict(message_value, orient='index')
    df=df.T.reset_index(drop=True)
    merge=pd.concat([df,merge]).reset_index(drop=True)
    print(message_value)








