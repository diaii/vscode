#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-27 13:56:21
LastEditTime : 2021-09-27 14:02:16
LastEditors  : 小鹿撞路
Description  : write message
FilePath     : \python_study\write_message.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write('I also love finding meaning in large datesets!\n')
    file_object.write('I love creating apps that can run in a broswer!\n')
