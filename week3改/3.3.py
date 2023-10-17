import re

def validate_id_number(id_number):
    #只有31日的月份
    pattern_31 = r"^[1-9]\d{5}(19|20)\d{2}(01|03|05|07|08|10|12)([0-2]\d|3[0-1])\d{3}(\d|x|X)$"
    #只有30日的月份
    pattern_30 = r"^[1-9]\d{5}(19|20)\d{2}(04|06|09|11)([0-2]\d|30)\d{3}(\d|x|X)$"
    #2月：平年28日，闰年29日
    pattern_2829 = r"^[1-9]\d{5}(19|20)\d{2}02[0-2][1-9]\d{3}(\d|x|X)$"
    if re.match(pattern_31, id_number) or re.match(pattern_30, id_number) or re.match(pattern_2829, id_number):
        return True
    else:
        return False

id_number = input("输入身份证号: ")
if validate_id_number(id_number):
    print("合法")
else:
    print("不合法")
