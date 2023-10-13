#设计一个求3次方根的算法(不允许直接调用求方根的函数)，并给出对应的Python程序

# def cube_root(num):
#     return num ** (1/3)

# num = float(input("请输入一个数字："))
# cubic_root = cube_root(num)
# print("数字的3次方根为:", cubic_root)

'''
这种算法的原理很简单,我们仅仅是不断用(x,f(x))的切线来逼近方程x^2-a=0的根。
根号a实际上就是x^2-a=0的一个正实根,这个函数的导数是2x。也就是说,函数上任一点(x,f(x))处的切线斜率是2x。
那么,x-f(x)/(2x)就是一个比x更接近的近似值。
代入 f(x)=x^2-a得到x-(x^2-a)/(2x),也就是(x+a/x)/2。
'''

#牛顿迭代
def cube_root(n):
    epsilon=1e-6
    g=n/2.0
    while abs(g**3-n)>epsilon:
        g=(2*g+n/g**2)/3.0
    return g

n=float(input("请输入一个数："))
result=cube_root(n)
print("%d三次方根是:",result)
