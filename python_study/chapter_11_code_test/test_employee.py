#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 17:08:54
LastEditTime : 2021-09-29 17:34:27
LastEditors  : 小鹿撞路
Description  : test_employee.py
FilePath     : \python_study\chapter_11_code_test\test_employee.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ 编写一个测试Employee类的测试 """

    def setUp(self):
        """ 创建一个雇员实例，以供测试方法使用 """
        self.first_employee = Employee('ryan', 'reynolds')

    def test_give_default_raise(self):
        """ 将年薪增加5000 """
        self.first_employee.give_raise()

    def test_give_custom_raise(self):
        """ 自定义年薪增加多少 """
        salary_increase = 6700  #此处自定义为6700 input('Your salary increase is: ')
        self.first_employee.give_raise(int(salary_increase))

unittest.main()