from eqsmart.main.remote_call import RemoteCall


def service(name='', age=0, phone='', id_card=''):
    res = RemoteCall('data_generation/user_generation').func_call((name, age, phone, id_card))
    return res
