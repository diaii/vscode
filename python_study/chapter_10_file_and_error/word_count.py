#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-27 14:51:54
LastEditTime : 2021-09-27 14:58:40
LastEditors  : 小鹿撞路
Description  : 计算一个文件大致包含多少个单词
FilePath     : \python_study\word_count.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


def count_words(file_name):
    """ 计算一个文件大致包含多少个单词 """
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + file_name + " doesn't exist!"
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " +
              str(num_words) + " words!")


file_names = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']
for file_name in file_names:
    count_words(file_name)
