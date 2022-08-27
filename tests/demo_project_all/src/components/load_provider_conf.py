from eqsmart.components.load_conf import LoadConf
import sys


class ProviderServerConf(LoadConf):
    def __init__(self, path):
        run_params = {}
        run_params_list = sys.argv[1:]
        for item in run_params_list:
            info = item.split('=')
            run_params[info[0]] = info[1]
        print('[app] 应用启动参数', run_params)  # {'env': 'dev', 'port': '7801'}
        super().__init__(path, run_params)

    def read_server(self):
        return {
            'PORT': self.node_read('provider.port'),
            'BUF_SIZE': self.node_read('provider.buf_size'),
            'BACKLOG': self.node_read('provider.backlog')
        }
