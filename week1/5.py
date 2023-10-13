x = float(input("请输入第一个数 x: "))
y = float(input("请输入第二个数 y: "))
z = float(input("请输入第三个数 z: "))

# 使用列表存储这三个数
numbers = [x, y, z]

# 使用sort函数对列表进行排序
numbers.sort()

# 使用循环打印排序后的结果
for num in numbers:
    print(num)