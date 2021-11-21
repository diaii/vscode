#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-28 21:23:49
LastEditTime : 2021-09-28 22:50:55
LastEditors  : 小鹿撞路
Description  : addition
FilePath     : \python_study\addition.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit!")

while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':    # 如果用户输入'q'则退出循环
        break
    # 第一种判断方式
    """ elif first_number.isdigit():
        first_number
    else:
        print("You can only enter a number to add!\nOr enter 'q' to quit!")
        continue """ 
    # 第二种判断方式
    try:
        float(first_number)    # 判断用户输入的类型是不是数字
    except ValueError:
        print("You can only enter a number to add!\nOr enter 'q' to quit!")
        continue

    while True:
        second_number = input('\nSecond number:')
        if second_number == 'q':
            break
        try:
            float(second_number)
            break     # 如果得到第二个数字，则退出第二个数字的循环
        except ValueError:
            print("You can only enter a number to add!\nOr enter 'q' to quit!")
            continue
    
    if second_number == 'q':
        break
    else:
        answer = float(first_number) + float(second_number)
        print(answer)
