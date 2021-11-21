#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-27 14:44:10
LastEditTime : 2021-09-27 14:49:15
LastEditors  : 小鹿撞路
Description  : alice 统计alice.txt 大约有多少个单词
FilePath     : \python_study\alice.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


file_name = 'alice.txt'

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry. thefile" + file_name + " doesn't exist!"
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words!")
