#!/usr/bin/env python
# coding=utf-8
# """
# Author       : 小鹿撞路
# Date         : 2021-09-26 14:16:51
# LastEditTime : 2021-09-26 14:18:13
# LastEditors  : 小鹿撞路
# Description  : user
# FilePath     : \python_study\user.py
# self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
# """

class User():
    """创建一个名为User的类"""

    def __init__(self, first_name, last_name, job, hobby):
        """ 初始化描述user的类 """
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        """ 打印用户信息摘要 """
        print(f"""First_name:{self.first_name.title()}
Last_name:{self.last_name.title()}
Job:{self.job.title()}
Hobby:{self.hobby.title()}""")

    def greet_user(self):
        """向用户发出个性化的问候"""
        print('Hello '+self.first_name.title()+' '+self.last_name.title()+'!')

    def increment_login_attempts(self):
        """ 将登陆次数递增1 """
        self.login_attempts += 1
        
    def read_login_attempts(self):
        """ 打印登陆次数 """
        print('You have already attempts '+str(self.login_attempts)+' times!')

    def reset_login_attempts(self):
        """ 重置登陆次数 """
        self.login_attempts = 0

Renolds = User('ryan', 'reynolds', 'actor', 'fishing')
Renolds.describe_user()
Renolds.greet_user()

Renolds.increment_login_attempts()  #登陆次数尝试增加4次
Renolds.read_login_attempts()
Renolds.increment_login_attempts()
Renolds.read_login_attempts()
Renolds.increment_login_attempts()
Renolds.read_login_attempts()
Renolds.increment_login_attempts()
Renolds.read_login_attempts()

Renolds.reset_login_attempts()  #重置登陆次数
Renolds.read_login_attempts()
