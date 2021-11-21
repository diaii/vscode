#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-26 16:53:16
LastEditTime : 2021-09-26 17:12:27
LastEditors  : 小鹿撞路
Description  : privileges
FilePath     : \python_study\privileges.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''


class User():
    """创建一个名为User的类"""

    def __init__(self, first_name, last_name):
        """ 初始化描述user的类 """
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """ 打印用户信息摘要 """
        print(f"""First_name:{self.first_name.title()}
Last_name:{self.last_name.title()}""")

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


class Admin(User):
    """ 创建一个名为Admin的子类 """

    def __init__(self, first_name, last_name):
        """ 初始化父类的属性，再初始化Admin所特有的属性 """
        super().__init__(first_name, last_name)
        self.privileges = Previleges()


class Previleges():
    """ 创建一个名为Previleges的类 """

    def __init__(self):
        """ 初始化类 """
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        """ 显示特权 """
        for privilege in self.privileges:
            print('-'+privilege)

    def add_privileges(self, *add_previleges):
        """ 增加特权 """
        for add_previlege in add_previleges:
            self.privileges.append(add_previlege)


first_admin = Admin('ryan', 'renolds')
first_admin.describe_user()
first_admin.privileges.show_privileges()

first_admin.privileges.add_privileges('can group email')
first_admin.privileges.show_privileges()