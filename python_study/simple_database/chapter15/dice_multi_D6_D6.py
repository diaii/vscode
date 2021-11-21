#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-19 17:19:59
LastEditTime : 2021-11-19 20:57:06
LastEditors  : 小鹿撞路
Description  : 掷两个6面骰子点数相乘
FilePath     : \simple_database\dice_multi_D6_D6.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''
import pygal

from die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果储存在一个列表中
results = [die_1.roll()*die_2.roll() for roll_num in range(5000)]


# 分析结果
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in list(
    set([die_1.roll()*die_2.roll() for roll_num in range(5000)]))]


# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 Dice 5000 times."
L = list(set([x1 * x2 for x1 in range(1, die_1.num_sides+1)
                     for x2 in range(1, die_2.num_sides+1)]))
L.sort()
hist.x_labels = L
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_multi_D6_D6.svg')
