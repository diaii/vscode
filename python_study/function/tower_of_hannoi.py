#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-14 21:43:35
LastEditTime : 2021-09-14 21:43:35
LastEditors  : 小鹿撞路
Description  : 汉诺塔问题
FilePath     : \python_study\function\tower_of_hannoi.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''
def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)  #直接搬过去
    else:
        move(n-1,a,c,b)    #把a上面的n-1移动到b
        move(1,a,b,c)      #把a的最后一块移动到c
        move(n-1,b,a,c)    #把b上面的n-1移动到c

move(4,'A','B','C') #调用函数