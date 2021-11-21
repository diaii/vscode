#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 10:18:30
LastEditTime : 2021-09-29 12:17:56
LastEditors  : 小鹿撞路
Description  : 喜欢的数字
FilePath     : \python_study\favorite_number.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import json

# 如果用户存储了最喜欢的数字，就打印它
# 否则，就提示用户输入它并存储它
filename = "favorite_number.txt"

try:    
    with open(filename) as file_object:
        favorite_number = json.load(file_object)
except FileNotFoundError:
    favorite_number = input('Your favorite number:')
    with open(filename,'w') as file_object:
        json.dump(favorite_number,file_object)
else:
    print("Your favorite number is " + favorite_number)
