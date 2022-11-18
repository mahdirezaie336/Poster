import json
import pika

from .secret import AMQP_URL


class RabbitMQ:

    def __init__(self, queue_name='hello'):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def publish(self, message: dict):
        self.channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(message).encode())
        print(" [x] Sent %r" % message)

    def start_receiving(self, callback=None):
        if callback is None:
            def callback(ch, method, properties, body):
                print(" [x] Received %r" % body)

        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)

        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.connection.close()
            print(' [*] Connection closed')

    def close(self):
        self.connection.close()
