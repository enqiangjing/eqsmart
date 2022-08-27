from eqsmart.main.remote_call import RemoteCall


def service(name, age):
    # req = {'name': name, 'age': age}
    req = (name, age)
    res = RemoteCall('user_service/other_service/son_service/abx').func_call(req)
    return res
