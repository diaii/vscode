#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-18 21:18:53
LastEditTime : 2021-11-18 21:44:07
LastEditors  : 小鹿撞路
Description  : 立方散点图
FilePath     : \simple_database\scatter_cubes.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x*x*x for x in x_values]

plt.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.autumn_r)

plt.title('Scatter of Cubes', fontsize=18)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Value of Cubes', fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.axis([0,100,0,1000000])
plt.show()
