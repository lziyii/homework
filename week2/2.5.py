def Square_root_3():
    c = 2000
    g = c / 2
    i = 0
    while abs(g * g - c) > 0.00000000001:
        g = (g + c / g) / 2
        i = i + 1
        print("%d:%.13f" % (i, g))

Square_root_3()

"""
结果：
c=2
1:1.5000000000000
2:1.4166666666667
3:1.4142156862745
4:1.4142135623747

c=200
1:51.0000000000000
2:27.4607843137255
3:17.3719487437960
4:14.4423809486623
5:14.1452565514874
6:14.1421359680227
7:14.1421356237310

c=2000
1:501.0000000000000
2:252.4960079840319
3:130.2084626463296
4:72.7842236959815 
5:50.1313529804782 
6:45.0132729652318
7:44.7223060868324
8:44.7213595600124
9:44.7213595499958
"""
