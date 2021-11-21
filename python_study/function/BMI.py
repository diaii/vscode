#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-12 20:39:42
LastEditTime : 2021-09-13 13:25:56
LastEditors  : 小鹿撞路
Description  : 计算BMI
FilePath     : \python_study\BMI.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

height = float(input('你的身高是(单位/m) '))
weight = float(input('你的体重是(单位/kg) '))
BMI = weight / (height * height)  # BMI等于体重除以身高的平方
BMI = float('%.2f' % BMI)  # 对BMI保留两位小数
print('你的BMI是：', BMI)

if BMI >= 32:
    print('严重肥胖')
elif BMI >= 28:
    print('肥胖')
elif BMI >= 25:
    print('过重')
elif BMI >= 18.5:
    print('正常')
else :
    print('过轻')