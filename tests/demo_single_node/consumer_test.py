from eqsmart.main.consumer import Consumer


def main():
    """"""
    '''实际使用时，连接注册中心，获取远程服务的地址和端口号'''
    server_conf = {
        # 远程服务器地址
        'IP': '11.11.0.127',
        # 远程服务器端口
        'PORT': 7881,
        # 消息读取长度
        'BUF_SIZE': 1024
    }
    '''组装rpc调用报文'''
    send_data = {
        'type': 'call provider',
        'service_name': 'user_service',
        'func': 'login',
        'args': (),
        'kwargs': {'name': '2', 'email': '4', 'phone': '5'}
    }
    Consumer(server_conf).func_call_int(send_data)


if __name__ == '__main__':
    main()
