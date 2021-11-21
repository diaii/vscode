#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 14:20:55
LastEditTime : 2021-09-29 14:41:47
LastEditors  : 小鹿撞路
Description  : test cities
FilePath     : \python_study\chapter_11_code_test\test_cities.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import unittest
from city_functions import get_city_country

class CityCountryTest(unittest.TestCase):
    """ 测试 city_functions.py """

    def test_city_country(self):
        """ 能够正确处理像 Beijing，China这样的案例吗 """
        city_country = get_city_country('beijing', 'china')
        self.assertEqual(city_country, 'Beijing, China')

    def test_city_country_population(self):
        """ 能够正确处理像 Beijing, China -population: 1300000000 people!"""
        city_country_population = get_city_country('beijing', 'china', 1300000000)
        self.assertEqual(city_country_population, 'Beijing, China -population: 1300000000 people!')


unittest.main()