def cube_root(n):
    epsilon = 1e-6
    g = n / 2.0
    while abs(g**3 - n) > epsilon:
        g = (2 * g + n / g**2) / 3.0
    return g

c = 10
result = cube_root(c)
print("%d的三次方根是:%.13f" % (c, result))
