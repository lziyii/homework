def find_max_list(n):
    a = n % 3
    b = n//3
    result = []
    if a == 0:
        for i in range(b):
            result.append(3)
    elif a == 1:
        result.append(2)
        result.append(2)
        for i in range(b - 1):
            result.append(3)
    else:
        result.append(2)
        for i in range(b):
            result.append(3)
    return result

num =int(input())
print(find_max_list(num))

'''
1.667个3
2. 经观察总结，所得数列只有2、3.
因此用该数除以3，考虑余数。若余数为0，则全为3；若为1，则需要两个2，其余全为3；若为2，则需要一个2，其余全为3.
'''