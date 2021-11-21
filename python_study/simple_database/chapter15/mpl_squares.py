#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-18 19:53:40
LastEditTime : 2021-11-19 16:13:50
LastEditors  : 小鹿撞路
Description  : temp
FilePath     : \simple_database\mpl_squares.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # linewidth 设置折线图线条粗细

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='y', labelsize=14)

# 关闭坐标刻度
# plt.xticks([])

# 旋转刻度
# plt.xticks(input_values, rotation=70)

# 关闭坐标轴
# plt.axis('off')

frame = plt.gca()
# y 轴不可见
frame.axes.get_yaxis().set_visible(False)
# x 轴不可见
frame.axes.get_xaxis().set_visible(False)

plt.show()
