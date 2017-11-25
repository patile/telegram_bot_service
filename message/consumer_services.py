import pika, os
import json
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://user:password@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

channel.queue_declare(queue='warning')

def callback(ch, method, properties, body):
    my_json = body.decode('utf8').replace("'", '"')
    main_json = json.loads(my_json)
    print(main_json["test"])

channel.basic_consume(callback,
                      queue='warning',
                      no_ack=True)


channel.start_consuming()