#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-30 21:26:14
LastEditTime : 2021-09-30 22:01:44
LastEditors  : 小鹿撞路
Description  : scatter_squares
FilePath     : \chapter_11_generate_date\scatter_squares.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c= y_values, cmap = plt.cm.Blues, edgecolor = 'none',s=40)

# 设置图表标题并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Values', fontsize=14)
plt.ylabel('Square of Numbers', fontsize=14)

# 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()
