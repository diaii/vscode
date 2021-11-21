#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-27 14:11:18
LastEditTime : 2021-09-27 14:17:30
LastEditors  : 小鹿撞路
Description  : 访客名单，输入名字后打印一句问候语，并将一条记录存储在guest_book.txt中
FilePath     : \python_study\visitor_list.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

visitor_name = input('Please enter your name!\n')
print(visitor_name.title()+'! Welcome to python world!')

file_name = 'guest_book.txt'

with open(file_name,'a') as file_object:
    file_object.write(visitor_name.title()+' has visited!\n')
    