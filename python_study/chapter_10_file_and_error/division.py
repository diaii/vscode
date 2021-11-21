#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-27 14:29:33
LastEditTime : 2021-09-27 14:35:51
LastEditors  : 小鹿撞路
Description  : division
FilePath     : \python_study\division.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit!")

while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input('Second number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)