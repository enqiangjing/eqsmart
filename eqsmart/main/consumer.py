import socket
from json import dumps as json_dumps
from eqsmart.components.code_msg import sys_error, REMOTE_CALL_ERROR_CODE
import traceback


class Consumer:
    def __init__(self, provider_conf):
        """
        对象初始化
        :param provider_conf: 服务提供着地址及其他配置
        """
        self.server_conf = provider_conf

    def func_call_int(self, send_data):
        """
        消费者调用器对象（调用provider消费）
        :return: None
        """
        try:
            connect_provider = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print('[eqsmart] [consumer] [Socket创建] [ERROR]:' + str(e))
            print(traceback.format_exc())
            return json_dumps(sys_error('9001', str(e)))  # 套接字创建失败

        try:  # 连接服务提供者
            connect_provider.connect((self.server_conf['IP'], self.server_conf['PORT']))
            connect_provider.setblocking(True)  # 设置阻塞模式，等待Provider调用的返回
            print(f"[eqsmart] [consumer] connect provider success {self.server_conf['IP']}:{self.server_conf['PORT']}")
        except Exception as e:
            print('[eqsmart] [consumer] [连接Provider] [ERROR]:' + str(e))
            print(traceback.format_exc())
            return json_dumps(sys_error('9002', str(e)))  # 端口绑定失败

        send_data['ip'] = socket.gethostbyname(socket.gethostname())  # 获取到本机IP

        try:  # 发送信息到Provider
            connect_provider.sendall(bytes(json_dumps(send_data), encoding="utf8"))
            print('[eqsmart] [consumer] [Provider服务调用] [调用信息]:', json_dumps(send_data))
            data = connect_provider.recv(self.server_conf['BUF_SIZE'])
            print('[eqsmart] [consumer] [Provider服务调用] [响应信息]:', str(data, 'UTF-8'))
            res = data
        except Exception as e:
            print('[eqsmart] [consumer] [Provider服务调用] [ERROR]:' + str(e))
            print(traceback.format_exc())
            res = json_dumps(sys_error(REMOTE_CALL_ERROR_CODE, str(e)))  # 远程服务调用失败
        finally:
            connect_provider.close()  # 关闭与provider的连接
        return res
