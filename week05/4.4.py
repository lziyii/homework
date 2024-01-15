def select_sort(array):
    for i in range(len(array)):
        x = i  # min index
        for j in range(i, len(array)):
            if array[j] < array[x]:
                x = j
        array[i], array[x] = array[x], array[i]
    return array


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

input_str = input("请输入数组元素，以空格分隔：")
input_list = input_str.split()
array = [int(x) for x in input_list]
print(shell_sort(array))

# 当n在某个特定范围时，希尔排序的时间复杂度约为O(n^1.3）;最坏的情况下，时间复杂度为O(n^2),但是优于直接插入排序。空间复杂度为O(1)


