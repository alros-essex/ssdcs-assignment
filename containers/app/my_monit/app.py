import threading
from dependency_injector.wiring import Provide, inject

from rabbit_listener import RabbitListener
from rest_app import RestApp

from container import Container


@inject
def main(rabbit_listener: RabbitListener = Provide[Container.rabbit]):

    def start_rabbit_listener():
        rabbit_listener.run()

    t1 = threading.Thread(target = start_rabbit_listener)
    t1.start()

    t1.join()

if __name__ == "__main__":

    container = Container()

    # db
    container.config.db_user.from_env("DB_USER", default = 'root', as_ = str)
    container.config.db_password.from_env("DB_PASSWORD", default = 'password', as_ = str)
    container.config.db_host.from_env("DB_HOST", default = 'localhost', as_ = str)
    container.config.db_database.from_env("DB_DATABASE", 'my_monit', as_ = str)
    # rabbit
    container.config.rabbit_url.from_env("RABBIT_URL", default = 'localhost', as_= str)
    #

    container.wire(modules=[__name__])

    main()
