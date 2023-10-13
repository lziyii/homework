import random
import math

N = 1000000
c = 0
for i in range(N):
    x = random.uniform(2.0, 3.0)
    y = random.uniform(0.0, 12.5)

    if y <= x**2 + 4 * x * math.sin(x):
        c += 1

result = c / N * 12.5
print(result)
