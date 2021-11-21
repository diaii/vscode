#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-12 21:52:41
LastEditTime : 2021-09-14 22:27:42
LastEditors  : 小鹿撞路
Description  : 求绝对值
FilePath     : \python_study\function\abstest.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
