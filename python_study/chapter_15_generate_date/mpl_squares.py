#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-30 20:52:06
LastEditTime : 2021-09-30 21:24:25
LastEditors  : 小鹿撞路
Description  : 绘制简单的折线图
FilePath     : \chapter_11_generate_date\mpl_squares.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square numbers", fontsize=24)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
