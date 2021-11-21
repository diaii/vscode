#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 12:18:26
LastEditTime : 2021-09-29 13:20:42
LastEditors  : 小鹿撞路
Description  : remember me
FilePath     : \python_study\remember.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import json
 
def get_stored_username():
    """ 如果用户存储了用户名，就获取它 """
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        pass
    else:
        return username

def get_new_username():
    """ 提示用户输入用户名 """
    username = input("What is your name?\n")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def judge_user():
    """ 判断用户名是否正确,不是的话输入用户名并存储它 """
    username = get_stored_username()
    if username:
        print('Whether your name is '+ username + "!")
        answer = input("Enter 'y' to yes or 'n' to no!\n")
        while answer:
            if answer == 'y':
                greet_user()
                break
            elif answer == 'n':
                new_username = get_new_username()
                print("We'll remember you when you come back, " + new_username + '!\n')
                break
            else:  # 如果用户输入了其它，提示用户输入'y'或'n'
                print('Whether your name is '+ username + "!")
                answer = input("Please enter 'y' to yes or 'n' to no!\n") 
                 
def greet_user():
    """ 问候用户，并指出其名字 """
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!\n")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!\n')


judge_user()