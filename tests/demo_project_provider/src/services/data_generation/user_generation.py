import random

from tests.demo_project_provider.src.entities.People.TUser import TUser
from tests.demo_project_provider.src.components.identity_card.id_number_generation import create_identity_card_simple


def service(name='', age=0, phone='', id_card=''):
    if name == '':
        name_surname = ['赵', '钱', '孙', '李', '周', '吴', '王', '张', '刘', '马']
        name_fame = ['小信', '小新', '小宝', '花开花', '庆', '强', '留', '剑', '田', '名可名']
        name = random.choice(name_surname) + random.choice(name_fame)
    if age == '' or age == 0:
        age_select = [16, 18, 20, 40, 60, 70]
        age = random.choice(age_select)
    if phone == '':
        phone_top = ['176', '138', '199']
        phone_tail = ''
        for i in range(8):
            phone_tail = phone_tail + str(random.randint(0, 9))
        phone = random.choice(phone_top) + phone_tail
    if id_card == '':
        id_card = create_identity_card_simple()

    return TUser(name, age, phone, id_card).__data__()
