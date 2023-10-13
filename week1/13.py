'''
13.给定一个常数n(n>0)，求n的阶乘，
即n!=1X2X..·X(n-1)Xn。例如，4!=24, 5!=120。
'''

def factorial(n):
    if n==1:
        return n
    n=n*factorial(n-1)
    return n

n = int(input("请输入一个正整数："))
factorial_n = factorial(n)
print(n, "的阶乘为:", factorial_n)
