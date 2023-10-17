# 辗转相除法
def fun1(n, m):
    temp = n % m
    while temp != 0:
        n = m
        m = temp
        temp = n % m
    return m
num1 = int(input("输入num1: "))
num2 = int(input("输入num2: "))
gcd = fun1(num1, num2)
print("最大公约数为:", gcd)