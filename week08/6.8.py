#使用Seaborn绘制三种常见图形

import matplotlib.pyplot as plt
import numpy as np

# 创建数据集
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)


import seaborn as sns
import pandas as pd

# 创建数据集
data = pd.DataFrame({'x': x, 'y1': y1, 'y2': y2, 'y3': y3})

# 绘制折线图
sns.lineplot(data=data[['x', 'y1', 'y2', 'y3']])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])
plt.show()

# 绘制散点图
sns.scatterplot(data=data[['x', 'y1', 'y2', 'y3']])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])
plt.show()

# 绘制柱状图
x_labels = ['A', 'B', 'C', 'D', 'E']
y = [10, 15, 7, 12, 9]
sns.barplot(x=x_labels, y=y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()


