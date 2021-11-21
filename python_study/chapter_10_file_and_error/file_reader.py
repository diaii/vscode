#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-26 20:58:52
LastEditTime : 2021-09-26 21:22:15
LastEditors  : 小鹿撞路
Description  : file reader
FilePath     : \python_study\file_reader.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())