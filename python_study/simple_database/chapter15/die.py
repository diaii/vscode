#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-19 17:15:03
LastEditTime : 2021-11-19 20:25:18
LastEditors  : 小鹿撞路
Description  : 一个表示骰子的类
FilePath     : \simple_database\die.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

from random import randint

class Die():
    """ 表示一个骰子的类 """

    def __init__(self, num_sides=6):
        """ 骰子默认为6面 """
        self.num_sides = num_sides

    def roll(self):
        """ 返回一个位于1~6之间的随机值 """
        return randint(1, self.num_sides)