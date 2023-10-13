#分别用for和while循环实现对一个给定序列的倒排序输出。例如，给定L=[1,2,3,4,5]，输出为[5,4,3,2,1]

# 使用for循环实现
L = input("请输入一个序列，数字之间用空格分隔：").split()
print(L)
L = [int(num) for num in L]

for i in range(len(L)-1, -1, -1):
    '''不换行输出'''
    print(L[i], end=" ") 
    

# 使用while循环实现
L = input("请输入一个序列，数字之间用空格分隔：").split()
L = [int(num) for num in L]
i = len(L) - 1

while i >= 0:
    print(L[i], end=" ")
    i -= 1

