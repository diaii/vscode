#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-13 13:08:21
LastEditTime : 2021-09-13 13:29:32
LastEditors  : 小鹿撞路
Description  : 求解二元一次方程组
FilePath     : \python_study\quardratic.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


def quardratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')

    d = b**2 - 4*a*c
    if a == 0:
        print('该方程有且仅有一个解，x='+str(('%.2f' % (-c/b))))
    elif d < 0:
        print('该方程无解')
    elif d == 0:
        print('改方程有且仅有一个解，x='+str(('%.2f' % -b/(2*a))))
    elif d > 0:
        import math
        d = math.sqrt(d)
        x1 = (-b+d)/(2*a)
        x2 = (-b-d)/(2*a)
        print('该方程有两个解,x1='+str('%.2f' % x1), 'x2='+str('%.2f' % x2))
