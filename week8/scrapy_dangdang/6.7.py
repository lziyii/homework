#使用Matplotlib绘制三种常见图形

import matplotlib.pyplot as plt
import numpy as np

# 创建数据集
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# 绘制折线图
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.plot(x, y3, label='tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend()
plt.show()

# 绘制散点图
plt.scatter(x, y1, label='sin(x)')
plt.scatter(x, y2, label='cos(x)')
plt.scatter(x, y3, label='tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend()
plt.show()

# 绘制柱状图
x_labels = ['A', 'B', 'C', 'D', 'E']
y = [10, 15, 7, 12, 9]
plt.bar(x_labels, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()