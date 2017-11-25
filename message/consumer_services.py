import pika, os
import json
import psycopg2
import math
from db_config import config

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(config['host'],config['dbname'],config['user'],config['password'])
conn = psycopg2.connect(conn_string)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://user:password@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

channel.queue_declare(queue='warning')



def distance(self, lat1, long1, lat2, long2):
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

    try:
        pass ##get veteniary data


    except:
        pass
    my_json = body.decode('utf8').replace("'", '"')
    main_json = json.loads(my_json)
    main_json["test"]

    for


channel.basic_consume(ihbar_handler,
                      queue='warning',
                      no_ack=True)


channel.start_consuming()