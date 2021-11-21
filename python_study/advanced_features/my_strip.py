#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-14 22:24:33
LastEditTime : 2021-09-14 22:24:51
LastEditors  : 小鹿撞路
Description  : 删除字符串首尾空格
FilePath     : \python_study\advanced\my_strip.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

def my_strip(my_str):
    while my_str[:1] == ' ':
        my_str = my_str[1:]    #删除字符串开头空格
    while my_str[-1:] == ' ':
        my_str = my_str[:-1]   #删除字符串末尾空格
    return my_str