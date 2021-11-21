#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-19 15:04:11
LastEditTime : 2021-11-19 17:06:01
LastEditors  : 小鹿撞路
Description  : 随机漫步
FilePath     : \simple_database\random_walk.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

from random import choice

class RandomWalk():
    """ 生成一个随机漫步数据的类 """

    def __init__(self, num_points=5000):
        """ 初始化随机漫步的属性 """
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]
        self.get_step()

    def fill_walk(self):
        """ 计算随机漫步包含所有的点 """

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
    def get_step(self):
        """ 确定每次漫步的距离和方向 """

        # 决定前进方向以及沿这个方向前进的距离
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
