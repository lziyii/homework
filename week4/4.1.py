a = int(input("请输入一个大于1的自然数："))
if a > 1:
    for i in range(2, a):
        if a % i == 0:
            print("%d不是质数" % a)
            break

    else:
        print("%d是质数" % a)
else:
    print("输入值有误")
