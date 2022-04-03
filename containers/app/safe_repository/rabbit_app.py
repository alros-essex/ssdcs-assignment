import pika
import time

from storage import Storage

class RabbitApp():

    def __init__(self) -> None:
        self._storage = Storage()

    def run(self):
        disconnected = True
        while(disconnected):
            try:
                connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
                disconnected = False
            except Exception as error:
                time.sleep(5)
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        def callback(ch, method, properties, body):
            self._storage.insert(body)

        channel.basic_consume(queue='hello',
                              auto_ack=True,
                              on_message_callback=callback)
        channel.start_consuming()
