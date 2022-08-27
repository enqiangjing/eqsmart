def aab():
    return '1762201270'


def service(name, email, phone):
    return {
        'name': '静夜思' + name,
        'email': 'eq@163.com' + email,
        'phone': aab() + phone
    }
