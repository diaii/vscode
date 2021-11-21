#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 13:37:41
LastEditTime : 2021-09-29 14:10:50
LastEditors  : 小鹿撞路
Description  : name_function
FilePath     : \python_study\chapter_11_code_test\name_function.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


def get_formatted_name(first, last, middle = ''):
    """ Generate a neatly formatted full name. """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()