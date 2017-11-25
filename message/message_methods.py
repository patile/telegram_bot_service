import pika, os
import logging


class SendWarning:
    def __init__(self):

        self.url = os.environ.get('CLOUDAMQP_URL', 'amqp://user:password@localhost:5672/%2f')
        self.params = pika.URLParameters(self.url)
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel() # start a channel
        self.channel.queue_declare(queue='warning') # Declare a queue


    def warning_publish(self,warning_json):
        try:
            self.channel.basic_publish(exchange='',
                                  routing_key='warning',
                                  body=str(warning_json))
            print("Sent")
        except:
            print("Eroor")

    def __del__(self):
        self.connection.close()

