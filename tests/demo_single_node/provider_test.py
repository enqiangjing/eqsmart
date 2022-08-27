"""
测试程序
"""
from eqsmart.main.provider import Provider


class UserService:

    def login(self, name, email, phone):
        return {
            'name': '静夜思' + name,
            'email': 'eq@163.com' + email,
            'phone': '1111' + phone
        }


def main():
    server_list = {
        'user_service': UserService()
    }
    server_conf = {
        'PORT': 7881,
        'BUF_SIZE': 1024,
        'BACKLOG': 5
    }
    Provider(server_conf, server_list).server_init()


if __name__ == '__main__':
    main()
