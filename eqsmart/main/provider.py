import json
import socket
import sys
from threading import Thread
from eqsmart.components.protocol import *
from eqsmart.components.ext_lib import not_contain_key
from eqsmart.components.code_msg import sys_error
import traceback


class Provider:
    def __init__(self, provider_conf, server_info, server_list):
        self.provider_conf = {}
        self.server_info = server_info
        self.server_list = server_list
        # 设置服务提供者默认信息
        self.provider_conf['HOST'] = '127.0.0.1' if not_contain_key(provider_conf, 'HOST') else provider_conf['HOST']
        self.provider_conf['PORT'] = 7901 if not_contain_key(provider_conf, 'PORT') else provider_conf['PORT']
        self.provider_conf['BACKLOG'] = 5 if not_contain_key(provider_conf, 'BACKLOG') else provider_conf['BACKLOG']
        self.provider_conf['BUF_SIZE'] = 1024 if not_contain_key(provider_conf, 'BUF_SIZE') else provider_conf[
            'BUF_SIZE']
        self.provider_conf['IP'] = '127.0.0.1' if not_contain_key(provider_conf, 'IP') else provider_conf['IP']
        self.provider_conf['WEIGHT'] = 1 if not_contain_key(provider_conf, 'IP') else provider_conf['WEIGHT']

    def __send_data__(self):
        """
        provider向注册中心注册服务时发送的信息
        """
        register_data = []
        send_data = {  # 服务注册协议
            'type': 'provider register',
            'remote': {
                'ip': self.provider_conf['IP'],
                'port': self.provider_conf['PORT'],
                'weight': self.provider_conf['WEIGHT']
            },
            'service_name': '',
            'func': []
        }
        for item in self.server_info:
            send_data['service_name'] = item
            send_data['func'] = self.server_info[item]
            register_data.append(send_data.copy())
        return register_data

    def __func_call__(self, connect):
        """
        处理consumer调用
        """
        while True:  # 等待调用
            try:
                # recv(buffer_size) 接收TCP数据，数据以字符串形式返回，buffer_size 指定要接收的最大数据量
                data = connect.recv(self.provider_conf['BUF_SIZE'])
                data = str(data, 'UTF-8')
                if data == '':  # 接收到服务端空数据跳过循环（不做处理）
                    break
                data_json = json.loads(data)
                print('[eqsmart] [provider] 接收到客户端数据:', data_json)
                protocol_analysis(data_json)

                try:  # 接收到了provider的调用信息，进行解析和函数执行
                    call_func = self.server_list.copy()
                    for item in data_json['service_name']:
                        call_func = call_func[item]
                    method = getattr(call_func['func'], data_json['func'])
                    response = method(*tuple(data_json['args']), **data_json['kwargs'])
                except Exception as e:
                    print(e, traceback.format_exc())
                    response = sys_error('5503', str(e))

                print('[eqsmart] [provider] 返回给客户端数据:', response)
                connect.sendall(bytes(json.dumps(response, default=str).encode('utf-8')))
            except socket.error as e:
                print(str(e))
                break
        '''关闭客户端连接'''
        connect.close()

    def server_init(self, register):
        """
        provider远程服务提供者初始化
        :return: None
        """
        try:  # 创建套接字
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print('[eqsmart] [Provider] [初始化异常] ' + str(e))
            sys.exit()

        try:  # 绑定端口和地址
            # bind() 绑定地址(host,port)到套接字， 在AF_INET下，以元组(host,port)的形式表示地址
            server.bind((self.provider_conf['HOST'], self.provider_conf['PORT']))
            print('[eqsmart] [Provider Starting] ' + self.provider_conf['HOST'] + ':' + str(self.provider_conf['PORT']))
        except socket.error as e:
            print("[eqsmart] Bind failed!" + str(e))
            print(traceback.format_exc())
            sys.exit()
        print("[eqsmart] Provider bind complete!")

        send_data = self.__send_data__()
        for i in send_data:  # 启动线程，将服务添加到注册中心；多个服务时，注册多次。
            Thread(target=register, args=(i,)).start()

        # listen(backlog) 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5即可
        server.listen(self.provider_conf['BACKLOG'])
        print("[eqsmart] Provider now listening")

        while True:  # 等待consumer连接
            connect, addr = server.accept()  # accept() 被动接受TCP客户端连接,(阻塞式)等待连接的到来
            print("[eqsmart] Provider connected with %s:%s " % (addr[0], str(addr[1])))
            Thread(target=self.__func_call__, args=(connect,)).start()  # 启动线程处理consumer的调用
