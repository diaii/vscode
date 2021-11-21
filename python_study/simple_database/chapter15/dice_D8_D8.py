#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-19 17:19:59
LastEditTime : 2021-11-19 20:17:34
LastEditors  : 小鹿撞路
Description  : 掷6面和10面骰子
FilePath     : \simple_database\dice_D8_D8.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''
import pygal

from die import Die

# 创建一个D6
die_1 = Die(8)
die_2 = Die(8)

# 掷几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling D8 and D8 Dice 5000 times."
hist.x_labels = list(set([x1 + x2 for x1 in range(1, die_1.num_sides+1)
                     for x2 in range(1, die_2.num_sides+1)]))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_D8_D8.svg')
