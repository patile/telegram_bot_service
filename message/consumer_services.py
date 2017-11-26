import pika, os
import json
import psycopg2
import math
import requests


url = os.environ.get('CLOUDAMQP_URL', 'amqp://user:password@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='warning')



def distance(lat1, long1, lat2, long2):
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLong = math.radians(long2 - long1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLong / 2) * math.sin(dLong / 2) * math.cos(lat1) * math.cos(
        lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d###send to js side with ajax and time interval .



def ihbar_handler(ch, method, properties, body):
    my_json = body.decode('utf8').replace("'", '"')
    main_json = json.loads(my_json)
    print(main_json)
    r = requests.post("http://127.0.0.1:8000/api/patients/",json=main_json)
    if r.status_code == 201 :
        print("CREATED")
        print(main_json)
    else:
        print("CREATION ERROR")
        print(r.status_code)
        print(r.content)


channel.basic_consume(ihbar_handler,
                      queue='warning',
                      no_ack=True)


channel.start_consuming()