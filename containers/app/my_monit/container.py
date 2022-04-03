from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from rabbit_listener import RabbitListener
from storage import Storage
from storage_configuration import StorageConfiguration
from rabbit_configuration import RabbitConfiguration

class Container(containers.DeclarativeContainer):

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

    storage = providers.Singleton(
        Storage,
        storage_configuration = storage_configuration
    )

    rabbit = providers.Singleton(
        RabbitListener,
        configuration = rabbit_configuration,
        storage = storage
    )
