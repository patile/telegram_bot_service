import pika, os
import json
import psycopg2
import math
from db_config import config


try:
    conn = psycopg2.connect("dbname='test_database' user='emirozbir' host='127.0.0.1' password=''")
except:
    print("Connection Error")

cur = conn.cursor()
cur.execute(''' SELECT * from veterinary_veterinary''')


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
    return d


def ihbar_handler(ch, method, properties, body):
    vet_datas = cur.fetchall()
    my_json = body.decode('utf8').replace("'", '"')
    main_json = json.loads(my_json)

    for vet_data in vet_datas :
        tmp_distance_data = distance(main_json["latitude"],main_json["longitude"],int(vet_data[2]),int(vet_data[3]))

        if tmp_distance_data <= 1:
            print("HOOOO")
        else:
            print("HAAA")


channel.basic_consume(ihbar_handler,
                      queue='warning',
                      no_ack=True)


channel.start_consuming()