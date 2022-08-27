from eqsmart.components.read_conf import ReadConf


class ClientConf:
    def __init__(self, path):
        self.configuration = ReadConf(path)

    def read(self):
        return {
            'alive': self.configuration.__read__('app.consumer.alive')
        }
