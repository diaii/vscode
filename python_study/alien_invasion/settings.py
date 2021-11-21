#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-29 20:36:30
LastEditTime : 2021-09-30 17:23:40
LastEditors  : 小鹿撞路
Description  : 设置
FilePath     : \alien_invasion\settings.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

class Settings():
    """ 存储《外星人入侵》的所有设置的类 """

    def __init__(self):
        """ 初始化游戏的静态设置 """
        # 屏幕设置
        self.screen_width = 1520
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 3
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数的提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()  

    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3 
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1 

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """ 提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)