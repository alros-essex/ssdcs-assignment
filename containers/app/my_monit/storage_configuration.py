class StorageConfiguration():

    def __init__(self, user:str, password:str, host:str, database:str) -> None:
        self._user = user
        self._password = password
        self._host = host
        self._database = database

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def host(self):
        return self._host

    @property
    def database(self):
        return self._database