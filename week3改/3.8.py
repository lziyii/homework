# 1选择排序
def selectionsort(arr):
    for i in range(len(arr) - 1):
        # 最小数的索引
        minindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        # i不是最小时，将i和最小数交换
        if i != minindex:
            arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr


# 2归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 分割数组为两半
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 递归排序两半
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 合并已排序的两半
    sorted_arr = merge(left_half, right_half)

    return sorted_arr


def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # 将剩余的元素添加到合并列表中
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

#3插入排序
def insertionsort(arr):
    for i in range(len(arr)):
        preindex=i-1
        current=arr[i]
        while preindex>=0 and arr[preindex]>current:
            arr[preindex+1]=arr[preindex]
            preindex-=1
        arr[preindex+1]=current
    return arr

#生成随机数
import random
def generate_random_sequence(length):
    return [random.randint(1, 1000) for _ in range(length)]

# 不同长度的随机数列
sequence_lengths = [100, 1000, 10000]

import time
for length in sequence_lengths:
    sequence = generate_random_sequence(length)
    print(f"长度为 {length} 的数列：")
    
    random_list1= sequence.copy()
    start =time.perf_counter()
    result1= selectionsort(random_list1)
    end = time.perf_counter()
    print('选择排序运行时间: %s 秒'%(end-start))

    random_list2  = sequence.copy()  
    start =time.perf_counter()
    result2= merge_sort(random_list2)
    end = time.perf_counter()
    print('归并排序运行时间: %s 秒'%(end-start))

    random_list3 = sequence.copy() 
    start =time.perf_counter()
    result3= insertionsort(random_list3)
    end = time.perf_counter()
    print('插入排序运行时间: %s 秒'%(end-start))
    print("-------------------------------------------")
    

'''
选择排序：时间复杂度为O(n^2)，无论数组是否有序，都需要进行n^2次比较和n次交换。

归并排序：时间复杂度为O(nlogn)，无论数组是否有序，都需要进行nlogn次比较和nlogn次交换。

插入排序：时间复杂度为O(n)，对于递增数组，插入排序只需要进行n次比较和0次交换。因而，插入排序在递增数组上的运行效果最好，时间复杂度为O(n)。
'''