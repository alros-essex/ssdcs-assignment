class RabbitConfiguration():

    def __init__(self, url:str) -> None:
        self._url = url

    @property
    def url(self):
        return self._url