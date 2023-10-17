def insertionsort(arr):
    for i in range(len(arr)):
        preindex = i - 1
        current = arr[i]
        while preindex >= 0 and arr[preindex] > current:
            arr[preindex + 1] = arr[preindex]
            preindex -= 1
        arr[preindex + 1] = current
    return arr


input_str = input("请输入数组元素，以空格分隔：")
input_list = input_str.split()
array = [int(x) for x in input_list]
print(insertionsort(array))
