'''Main entrypoint for MyMonit'''

import threading
from dependency_injector.wiring import Provide, inject
from dependency_injector import containers, providers

from .rabbit_listener import RabbitListener, RabbitConfiguration, RabbitMessageProcessor
from .storage import Storage, StorageConfiguration
from .rest_listener import RestListener, RestConfiguration

class Container(containers.DeclarativeContainer):
    '''main configuration'''

    config = providers.Configuration()

    storage_configuration = providers.Singleton(
        StorageConfiguration,
        db_user = config.db_user,
        db_password = config.db_password,
        db_host = config.db_host,
        db_database = config.db_database
    )

    rabbit_configuration = providers. Singleton(
        RabbitConfiguration,
        rabbit_url = config.rabbit_url,
        rabbit_user = config.rabbit_user,
        rabbit_password = config.rabbit_password,
        rabbit_exchange = config.rabbit_exchange,
        rabbit_routing = config.rabbit_routing,
        rabbit_queue = config.rabbit_queue
    )

    rest_configuration = providers.Singleton(
        RestConfiguration,
        rest_host = config.rest_host
    )

    storage = providers.Singleton(
        Storage,
        storage_configuration = storage_configuration
    )

    message_processor = providers.Singleton(
        RabbitMessageProcessor,
        storage = storage
    )

    rabbit = providers.Singleton(
        RabbitListener,
        configuration = rabbit_configuration,
        message_processor = message_processor
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

#if __name__ == "__main__":
def init():
    container = Container()

    # db
    container.config.db_user.from_env("DB_USER", default = 'root', as_ = str)
    container.config.db_password.from_env("DB_PASSWORD", default = 'password', as_ = str)
    container.config.db_host.from_env("DB_HOST", default = 'localhost', as_ = str)
    container.config.db_database.from_env("DB_DATABASE", 'my_monit', as_ = str)
    # rabbit
    container.config.rabbit_url.from_env("RABBIT_URL", default = 'localhost', as_= str)
    container.config.rabbit_user.from_env("RABBIT_USER", default = 'guest', as_= str)
    container.config.rabbit_password.from_env("RABBIT_PASSWORD", default = 'guest', as_= str)
    container.config.rabbit_exchange.from_env("RABBIT_EXCHANGE", default = 'mymonit', as_= str)
    container.config.rabbit_routing.from_env("RABBIT_ROUTING", default = 'measures', as_= str)
    container.config.rabbit_queue.from_env("RABBIT_QUEUE", default = 'measures', as_= str)
    # rest
    container.config.rest_host.from_env("REST_HOST", default = "0.0.0.0", as_ = str)
    #

    container.wire(modules=[__name__])

    main()
