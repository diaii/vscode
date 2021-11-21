#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 14:58:19
LastEditTime : 2021-09-29 15:07:07
LastEditors  : 小鹿撞路
Description  : language_survey
FilePath     : \python_study\chapter_11_code_test\language_survey.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查AnonymousSurvey对象
question = "What language did you first to learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\n Thank you to everyone who participated in the survey!")
my_survey.show_results()