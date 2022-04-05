'''convert stdin in inputs for rabbit

run it with

$ tail -f my_input.txt | python3 generators/from_stdin.py

and keep adding values & saving my_input.txt
'''
import fileinput
import time
import json
import pika

RABBIT_HOST = 'localhost'
RABBIT_EXCHANGE = 'mymonit'
RABBIT_ROUTING = 'measures'
EXPERIMENT = 'device-vibrations'
MEASURE = 'hertz'


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST))
    channel = connection.channel()
    for line in fileinput.input():
        msg = {
            'experiment': EXPERIMENT,
            'measure': MEASURE,
            'value': float(line),
            'timestamp': int(time.time())
        }
        channel.basic_publish(exchange=RABBIT_EXCHANGE,
                              routing_key=RABBIT_ROUTING,
                              body=json.dumps(msg))
    connection.close()
