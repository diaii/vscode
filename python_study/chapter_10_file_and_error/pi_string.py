#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-26 21:24:26
LastEditTime : 2021-09-26 21:48:07
LastEditors  : 小鹿撞路
Description  : 
FilePath     : \python_study\pi_string.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print(pi_string.count(birthday))
else:
    print('no')

