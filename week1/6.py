w = float(input("请输入第一个数w:"))
x = float(input("请输入第二个数x:"))
y = float(input("请输入第三个数y:"))
z = float(input("请输入第四个数z:"))

# 创建一个列表并将四个数添加到列表中
numbers = [w, x, y, z]

# 使用sort()方法对列表进行排序，reverse=True表示降序排序
numbers.sort(reverse=True)

# 使用for循环逐个打印排序后的数
for num in numbers:
    print(num)
