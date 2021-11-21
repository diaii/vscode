#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-27 14:04:11
LastEditTime : 2021-09-27 14:07:15
LastEditors  : 小鹿撞路
Description  : 输入用户名，并将用户名储存在guest.txt
FilePath     : \python_study\enter_username.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

user_name = input('Please enter your user name!')

file_name = 'guest.txt'

with open(file_name,'a') as file_object:
    file_object.write(user_name.title()+'\n')