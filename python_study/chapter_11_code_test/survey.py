#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 14:47:10
LastEditTime : 2021-09-29 16:50:25
LastEditors  : 小鹿撞路
Description  : 测试类
FilePath     : \python_study\chapter_11_code_test\survey.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

class AnonymousSurvey():
    """ 手机匿名调查问卷的答案 """

    def __init__(self, question):
        """ 存储一个问题，并将存储答案做准备 """
        self.question = question
        self.responses = []

    def show_question(self):
        """ 显示调查问卷 """
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        """ 显示收集到的所有答案 """
        print("Survey results:")
        for response in self.responses:
            print(f"-{response}")
            