from tests.demo_project_provider.src.components.identity_card import area_list
from random import choice
import random


def create_identity_card_simple(birthday='', province_city_code=''):
    """
    生成身份证号码
    :param birthday: 生日
    :param province_city_code: 地区编码
    :return:
    """

    if province_city_code != '':
        area_num_simple = province_city_code
    else:
        area_num_simple = choice(area_list.area_num)

    if birthday == '':
        year = ['1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984',
                '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994'
                ]
        year_number = choice(year)
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
               '18', '19',
               '20', '21', '22', '23', '24', '25', '26', '27', '28']
        month_number = choice(month)
        day_number = choice(day)
        # 出生的年月日
        birthday_about = year_number + month_number + day_number
    else:
        birthday_about = birthday
        year_number = birthday_about[0:4]
        month_number = birthday_about[4:6]
        day_number = birthday_about[6:8]

    order_code = str(random.randint(100, 999))

    code = str((int(area_num_simple[0:1]) * 7 + int(area_num_simple[1:2]) * 9 + int(
        area_num_simple[2:3]) * 10 + int(area_num_simple[3:4]) * 5 +
                int(area_num_simple[4:5]) * 8 + int(area_num_simple[5:6]) * 4 + int(year_number[0:1]) * 2 + int(
                year_number[1:2]) * 1 + int(year_number[2:3]) * 6 +
                int(year_number[3:4]) * 3 + int(month_number[0:1]) * 7 + int(month_number[1:2]) * 9 + int(
                day_number[0:1]) * 10 + int(day_number[1:2]) * 5 +
                int(order_code[0:1]) * 8 + int(order_code[1:2]) * 4 + int(order_code[2:3]) * 2) % 11)

    code_number = ''
    if code == "0":
        code_number = "1"
    elif code == "1":
        code_number = "0"
    elif code == "2":
        code_number = "X"
    elif code == "3":
        code_number = "9"
    elif code == "4":
        code_number = "8"
    elif code == "5":
        code_number = "7"
    elif code == "6":
        code_number = "6"
    elif code == "7":
        code_number = "5"
    elif code == "8":
        code_number = "4"
    elif code == "9":
        code_number = "3"
    elif code == "10":
        code_number = "2"

    id_number = area_num_simple + birthday_about + order_code + code_number

    return id_number
