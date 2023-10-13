def calculate_product(arr):
    n = len(arr)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    for i in range(1, n):
        left_products[i] = left_products[i-1] * arr[i-1]
    
    for i in range(n-2, -1, -1):
        right_products[i] = right_products[i+1] * arr[i+1]
    
    for i in range(n):
        result[i] = left_products[i] * right_products[i]
    
    return result

n = input("数组中数的个数n：")
L =  input("输入n个数，用空格间隔：")
arr = [int(n) for n in L.split()]
result = calculate_product(arr)
print("B:", result)