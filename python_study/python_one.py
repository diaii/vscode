#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-08-26 18:27:35
LastEditTime : 2021-09-19 16:37:41
LastEditors  : 小鹿撞路
Description  : 
FilePath     : \python_study\python_one.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

# list1 = range(10)
# sum = 0
# for x in list1:
#    sum += x
# print(sum)


# n = 0

# while n < 10:
#     n += 1
#     if n % 2 == 0:
#         continue
#     print(n)

from functools import reduce
def str2float(s):
    def char2num(n):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                  '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[n]  # 把字符串转换成相对应的数字

    L = s.split('.')  # 用‘.’把一个字符串形式的float拆分成整数和小数部分组成的一个字符串列表
    num_integer = reduce(lambda x, y: x*10+y, map(char2num, L[0]))  # 转换出整数部分
    num_decimal = reduce(lambda x, y: x*10+y, map(char2num, L[1]))  # 转换出小数部分
    return num_integer + num_decimal/(10**(len(str(num_decimal))))  # 把整数和小数部分合成一个float

print(str2float('123.4564'))