'''Main entrypoint for MyMonit'''

import threading
from dependency_injector.wiring import Provide, inject
from dependency_injector import containers, providers

from rabbit_listener import RabbitListener, RabbitConfiguration
from storage import Storage, StorageConfiguration
from rest_listener import RestListener, RestConfiguration

class Container(containers.DeclarativeContainer):
    '''main configuration'''

    config = providers.Configuration()

    storage_configuration = providers.Singleton(
        StorageConfiguration,
        user = config.db_user,
        password = config.db_password,
        host = config.db_host,
        database = config.db_database
    )

    rabbit_configuration = providers.Singleton(
        RabbitConfiguration,
        url = config.rabbit_url
    )

    rest_configuration = providers.Singleton(
        RestConfiguration,
        rest_host = config.rest_host
    )

    storage = providers.Singleton(
        Storage,
        storage_configuration = storage_configuration
    )

    rabbit = providers.Singleton(
        RabbitListener,
        configuration = rabbit_configuration,
        storage = storage
    )

    rest = providers.Singleton(
        RestListener,
        configuration = rest_configuration
    )

@inject
def main(rabbit_listener: RabbitListener = Provide[Container.rabbit]):
    '''Kickstart the application'''
    def start_rabbit_listener():
        rabbit_listener.run()
    thread_rabbit = threading.Thread(target = start_rabbit_listener)
    thread_rabbit.start()
    thread_rabbit.join()

if __name__ == "__main__":
    container = Container()

    # db
    container.config.db_user.from_env("DB_USER", default = 'root', as_ = str)
    container.config.db_password.from_env("DB_PASSWORD", default = 'password', as_ = str)
    container.config.db_host.from_env("DB_HOST", default = 'localhost', as_ = str)
    container.config.db_database.from_env("DB_DATABASE", 'my_monit', as_ = str)
    # rabbit
    container.config.rabbit_url.from_env("RABBIT_URL", default = 'localhost', as_= str)
    # rest
    container.config.rest_host.from_env("REST_HOST", default = "0.0.0.0", as_ = str)
    #

    container.wire(modules=[__name__])

    main()
