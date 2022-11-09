"""
定义服务返回信息列表
"""

REMOTE_CALL_ERROR_CODE = '5501'


def response(code='default', msg='default', data=None):
    res = {
        'code': code,
        'msg': msg
    }
    if data is not None:
        res['data'] = data
    return res


def success(data=None):
    return response('2000', 'success', data)


def error(data=None):
    return response('5000', 'error', data)


def sys_error(code='9001', data=None):
    code_list = {
        REMOTE_CALL_ERROR_CODE: 'Remote call error!',
        '5502': 'Remote call error!',
        '5503': 'Remote function call error!',
        '9001': 'Socket creation failed!',
        '9002': 'Socket bind failed!',
    }
    print(code_list)
    res = {'code': code, 'msg': code_list[code]}
    if data is not None:
        res['data'] = data
    return res


if __name__ == '__main__':
    sys_error()
