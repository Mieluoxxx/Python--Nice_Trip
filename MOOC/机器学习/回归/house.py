import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model


# 读取数据集
datasets_X = []                         #*房屋尺寸
datasets_Y = []                         #*房屋成交价格
fr = open('prices.txt','r')             #*打开数据集
lines = fr.readlines()                  #*一次性读取
for line in lines:                      #*循环遍历
    items = line.strip().split(',')     #*去除逗号
    datasets_X.append(int(items[0]))    #*转换为int型
    datasets_Y.append(int(items[1]))

length = len(datasets_X)                #*数据总数
datasets_X = np.array(datasets_X).reshape([length,1])   #*转化为数组并成为二维衣服和线性回归拟合函数要求
datasets_Y = np.array(datasets_Y)                       #*数组

minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX,maxX).reshape([-1,1])#*以最大最小值为单位建立等差数列


linear = linear_model.LinearRegression()#*调用线型回归模块建立回归方程，拟合数据 
linear.fit(datasets_X, datasets_Y)

# 图像中显示
plt.scatter(datasets_X, datasets_Y, color = 'red')  #*绘制散点
plt.plot(X, linear.predict(X), color = 'blue')      #*绘制直线
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()