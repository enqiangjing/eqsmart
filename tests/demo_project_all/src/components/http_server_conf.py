from eqsmart.components.read_conf import ReadConf


class ServerConf:
    def __init__(self, path):
        self.configuration = ReadConf(path)

    def read(self):
        return {
            'PORT': self.configuration.__read__('app.http.port')
        }
