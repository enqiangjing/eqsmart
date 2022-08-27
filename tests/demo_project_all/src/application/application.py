from eqsmart.components.scan_services import ScanServices
from eqsmart.components.read_module import ReadModule
from eqsmart.main.provider import Provider
from eqsmart.main.http_servr import http_server
from eqlink.main.clent import LinkClient
from eqlink.main.register import LinkRegister
from threading import Thread

'''
扫描服务表
scan_services: Provider服务
scan_http_services: Http服务
'''
scan_services = ScanServices('../services')
scan_http_services = ScanServices('../webs')

'''组件加载器'''
read_components_module = ReadModule('../components')


class Register:
    def __init__(self, path):
        """
        注册中心连接工具初始化
        :param path: 配置文件路径
        """
        ''' 注册中心的配置信息 '''
        self.link_conf = read_components_module.read('link_server_conf').ServerConf(path).read()
        ''' 服务消费者配置信息 '''
        self.consumer_conf = read_components_module.read('consumer_client_conf').ClientConf(path).read()

    def register(self):
        """
        Provider到注册中心的注册器
        :return: 注册器
        """
        return LinkRegister(self.link_conf)

    def keep_connect(self):
        """
        Consumer与注册中心的连接器
        :return: 连接器
        """
        return LinkClient(self.link_conf, self.consumer_conf)


class Application:
    def __init__(self, path):
        """
        app初始化
        :param path: 配置文件路径
        """
        self.conf_path = path
        ''' Provider服务列表扫描 '''
        self.services = scan_services.get_services()
        self.services_class = scan_services.get_services_class()
        self.provider_conf = read_components_module.read('load_provider_conf').ProviderServerConf(path).read_server()
        ''' HTTP服务列表扫描 '''
        self.http_services = scan_http_services.get_services()
        self.http_services_class = scan_http_services.get_services_class()
        self.http_conf = read_components_module.read('http_server_conf').ServerConf(path).read()

    def __provider__(self):
        """
        提供服务的Provider启动并注册
        :return: void
        """
        Provider(self.provider_conf, self.services, self.services_class).server_init(
            Register(self.conf_path).register().register_int)

    def __connect_link__(self):
        """
        Consumer启动并保持与注册中心的连接
        :return: void
        """
        Register(self.conf_path).keep_connect().client_int({'type': 'get provider'})

    def __http_server__(self):
        """
        供WEB访问的HTTP服务启动
        :return: void
        """
        http_server(self.http_conf, self.http_services_class).serve_forever()


def main():
    m = Thread(target=Application('./app.yaml').__provider__)
    c = Thread(target=Application('./app.yaml').__connect_link__)
    w = Thread(target=Application('./app.yaml').__http_server__)
    m.start()  # Provider启动
    c.start()  # Consumer连接器启动
    w.start()  # WEB服务启动


def test():
    scan_http_services.get_services()
    print(scan_http_services.get_services_class())


if __name__ == '__main__':
    main()
