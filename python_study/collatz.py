#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-25 14:09:41
LastEditTime : 2021-09-25 15:00:15
LastEditors  : 小鹿撞路
Description  : Collatz序列
FilePath     : \python_study\collatz.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


def collatz(number):
    if number % 2 == 0:
        num = number//2   # '//'表示向下取接近商的整数
        print(num)
    else:
        num = 3*number+1
        print(num)
    return num


# This is Collatz sequence.
print('This is Collatz sequence.')

print('Please enter an Int number')
try:
    inputNumber = int(input())
    inputNumbers = inputNumber  #方便最后一行打印计算次数
    countNumber = 0
    while inputNumber != 1:
        countNumber += 1
        inputNumber = collatz(inputNumber)
    else:
        print('Done')
except:
    print('Error:Type error, int are allowed')

print(str(inputNumbers)+' to 1 needs to count '+str(countNumber)+' times')
