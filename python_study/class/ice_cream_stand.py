#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-26 16:01:53
LastEditTime : 2021-09-26 16:28:31
LastEditors  : 小鹿撞路
Description  : ice cream stand
FilePath     : \python_study\ice_cream_stand.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

class Restaurant():
    """ 创建一个名为Restaurant的类 """

    def __init__(self,restrarant_name,cuisine_type):
        """ 初始化描述餐馆的类 """
        self.restaurant_name = restrarant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆的信息"""
        print('\nRestaurant name: '+self.restaurant_name.title())
        print('Cuisine type: '+self.cuisine_type)

    def open_restaurant(self):
        """ 打印这家餐馆正在营业 """
        print(self.restaurant_name.title()+' is open!')

    def set_number_served(self,served):
        """ 设定就餐人数 """
        if served >= self.number_served:
            self.number_served = served
        else:
            print('Something wrong!')

    def read_number_served(self):
        """ 打印就餐过的人数 """
        print('This restaurant have '+ str(self.number_served)+' people served!')

    def increment_number_served(self,add_served):
        """增加就餐人数"""
        self.number_served += add_served


class IceCreamStand(Restaurant):
    """ 创建一个名为冰淇淋小店的餐馆子类 """

    def __init__(self,restaurant_name,cuisine_type,*flavors):
        """ 初始化父类的属性，再初始化冰淇淋小店特有的属性 """
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def make_ice_cream(self):
        """ 打印冰淇淋的口味 """
        print(self.restaurant_name.title()+' has the following flavors:')
        for flavor in self.flavors:
            print('-'+ flavor)


my_ice_cream_stand = IceCreamStand('ice town','frozen','vanilla','strawberry','chocolate')
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.make_ice_cream()

his_ice_cream_stand = IceCreamStand('mixue ice town','frozen','apple','banana')
his_ice_cream_stand.describe_restaurant()
his_ice_cream_stand.make_ice_cream()