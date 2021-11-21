#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 16:38:25
LastEditTime : 2021-09-29 17:13:02
LastEditors  : 小鹿撞路
Description  : test_survey.py
FilePath     : \python_study\chapter_11_code_test\test_survey.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ 针对AnonymousSurvey类的测试 """

    def setUp(self):
        """ 创建一个调查对象和一组答案，供使用的测试方法使用 """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_responde(self):
        """ 测试单个答案时会被妥善地存储 """
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        """ 测试三个答案会被妥善地保存 """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()