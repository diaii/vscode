#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 09:23:55
LastEditTime : 2021-09-29 09:23:55
LastEditors  : 小鹿撞路
Description  : 读取文件，并把文件打印在屏幕上
FilePath     : \python_study\read_file.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

def read_file(file_name):
    """ 读取文件，并把文件打印在屏幕上 """
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        # 文件不存在时提示文件不存在
        msg = "Sorry, the file "+file_name+" does not exist."
        print(msg)
  

file_names = ["cats.txt","dogs.txt"]
for file_name in file_names:
    read_file(file_name)