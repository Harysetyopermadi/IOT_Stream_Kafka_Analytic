from flask import Flask, request, jsonify
import json,time,random
from datetime import datetime
from kafka import KafkaProducer

app = Flask(__name__)
@app.route('/', methods=['POST'])
def data_terima():
    # Get the 'name' value from the request headers
    # Create a custom response
    cnt=0
    for a in range(10):
        if cnt<=5:
            try:
                data_dic = {}
                
                args = request.headers
                name = args.get('name')
                temperature = args.get('temperature')
                kelembaban = args.get('kelembaban')
                cahaya = args.get('cahaya')
                regional = args.get('regional')
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                data_dic['name'] = name
                data_dic['temperature'] = float(temperature)
                data_dic['kelembaban'] = (float(kelembaban)/1024)*100
                data_dic['cahaya'] = (float(cahaya)/1024)*100
                data_dic['regional'] = regional
                data_dic['time'] = time_now
                
                print(name)
                producer = KafkaProducer(
                bootstrap_servers='192.168.0.5:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
                producer.send('belajar-IOT', value=data_dic)
                response_data = {'message': f'Hello, {name}! Your request was received successfully.'}
                break
            except:
                pass
        else: 
            response_data ={'message':'Your Request Failed'}
            break
        time.sleep(1)
        cnt=cnt+1

    # Return the response as JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.5', port=8080)
