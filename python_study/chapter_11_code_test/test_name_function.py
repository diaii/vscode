#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 13:55:10
LastEditTime : 2021-09-29 14:22:08
LastEditors  : 小鹿撞路
Description  : 单元测试和测试用例
FilePath     : \python_study\chapter_11_code_test\test_name_function.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """ 测试name_function.py """

    def test_first_last_name(self):
        """ 能够正确地处理像Janis Joplin这样的姓名吗？ """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ 能够正确处理像 Wolfgang Amadeus Mozart 这样的姓名吗 """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual = (formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()  #让python 运行这个文件中的测试