#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 17:02:38
LastEditTime : 2021-09-29 17:32:37
LastEditors  : 小鹿撞路
Description  : employee
FilePath     : \python_study\chapter_11_code_test\employee.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


class Employee():
    """ 编写一个雇员的类 """

    def __init__(self, first_name, last_name):
        """ 初始化类 ，接受姓，名，还有年薪"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = 6000

    def give_raise(self, salary_increase=5000):
        """ 将年薪增加5000 """
        self.annual_salary += salary_increase
        # print(f"{self.first_name} {self.last_name}'s annual salary is {self.annual_salary} now!")
        return self.annual_salary

