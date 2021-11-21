#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-19 15:20:13
LastEditTime : 2021-11-19 16:39:34
LastEditors  : 小鹿撞路
Description  : 随机漫步
FilePath     : \simple_database\rw_visual.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活跃状态，就不断模拟随机漫步
while True:

    # 创建一个RandomWalk 实例，并将其包含的点绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口尺寸
    plt.figure(figsize=(16, 10))

    # 隐藏坐标
    """ current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False) """

    """隐藏坐标代码中，须将plt.axes()赋给一个变量，get_xaxis,get_yaxis要改为xaxis，yaxis，否则程序无效"""
    """还有就是set_visible(False)要放在plt.scatter之前，否则就不能绘制出点图"""

    # 绘制随机漫步图并做颜色映射
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.autumn, s=1)
    
    # 绘制起点和终点
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', s=100)

    # 关闭坐标轴
    plt.axis('off')

    
    plt.show() 

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
