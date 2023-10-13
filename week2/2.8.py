# 1. Leibniz级数
import math

def leibniz_pi(n):
    pi = 0
    for i in range(n):
        term = (-1) ** i / (2 * i + 1)
        pi += term
    return pi * 4

n = 10000
result = leibniz_pi(n)
print("Leibniz级数:", round(result, 10))

# 2. 蒙特卡洛方法
import random

def monte_carlo_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
    pi = (inside_circle / n) * 4
    return pi

n = 10000
result = monte_carlo_pi(n)
print("蒙特卡洛方法:" "{:.10f}".format(result))

# 3.公式法
pi = 0
N = 10000
for k in range(N):
    pi += (
        1
        / pow(16, k)
        * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
    )

print("公式法:" "{:.10f}".format(pi))
