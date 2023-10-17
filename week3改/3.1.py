def decimal_to_binary(decimal_num):
    binary_num = ""
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part

    flag = 0
    while integer_part > 0:
        flag = 1
        binary_num = str(integer_part % 2) + binary_num
        integer_part = integer_part // 2

    if fractional_part != 0:
        # 整数部分非零
        if flag == 1:
            binary_num += "."
        # 整数部分为零
        else:
            binary_num += "0."

    while fractional_part != 0:
        fractional_part *= 2
        binary_num += str(int(fractional_part))
        fractional_part = fractional_part - int(fractional_part)

    return binary_num


decimal_num = float(input("输入一个十进制数: "))
binary_num = decimal_to_binary(decimal_num)
print("转化的二进制数: ", binary_num)
