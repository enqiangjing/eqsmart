from eqsmart.components.read_conf import ReadConf


class ServerConf:
    def __init__(self, path):
        self.configuration = ReadConf(path)

    def read(self):
        return {
            'IP': self.configuration.__read__('app.eqlink.ip'),
            'PORT': self.configuration.__read__('app.eqlink.port'),
            'BUF_SIZE': self.configuration.__read__('app.eqlink.buf_size'),
            'BACKLOG': self.configuration.__read__('app.eqlink.backlog'),
        }
