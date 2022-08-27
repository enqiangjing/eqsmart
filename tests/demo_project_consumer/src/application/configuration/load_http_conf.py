import sys

from eqsmart.components.load_conf import LoadConf, get_run_params


class HttpServerConf(LoadConf):
    def __init__(self, path):
        super().__init__(path, get_run_params(sys.argv[1:]))

    def read_server(self):
        return {
            'PORT': self.node_read('http.port'),
            'HOST': self.node_read('http.host')
        }
