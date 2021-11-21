#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-18 20:25:06
LastEditTime : 2021-11-19 11:56:02
LastEditors  : 小鹿撞路
Description  : 绘制散点图并设置其样式
FilePath     : \simple_database\scatter_squares.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=5)

# 设置图表标题并给坐标加上标签
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])  # x轴和y轴最小值最大值

# 保存图片 第一个参数为文件名，第二个参数将图表多余的空白区域裁减掉，若要保持，删除即可
plt.savefig("squares_plot.png", bbox_inches='tight')
