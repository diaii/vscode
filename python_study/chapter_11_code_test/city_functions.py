#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 14:17:35
LastEditTime : 2021-09-29 14:35:00
LastEditors  : 小鹿撞路
Description  : city_functions
FilePath     : \python_study\chapter_11_code_test\city_functions.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


def get_city_country(city, country, population = ''):
    if population:
        city_belongs = city.title() + ', ' + country.title() + ' -population: ' + str(population) +' people!'
    else:
        city_belongs = city.title() + ', ' + country.title()
    return city_belongs
