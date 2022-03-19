import socket
try:
        import json
except ImportError:
        import simplejson as json

logserver_ip   = 'localhost'
logserver_port = 5959
json_message   = {}

json_message['message']    = 'test'
json_message['sourcetype'] = 'Appl-Test'
json_message['logfile']    = '/tmp/test.log'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((logserver_ip, logserver_port))
s.send('app 1000APP app 55.3.244.1 GET /index.html 15824 0.043 other stuff'.encode())

s.close()