import threading

from rabbit_app import RabbitApp
from rest_app import RestApp

def start_rest():
    RestApp().run()

def start_rabbit():
    RabbitApp().run()

if __name__ == "__main__":
    t1 = threading.Thread(target=start_rest)
    t2 = threading.Thread(target=start_rabbit)

    t1.start()
    t2.start()
    # join the main thread
    t1.join()
    t2.join()