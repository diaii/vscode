#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-11-19 21:09:51
LastEditTime : 2021-11-20 14:40:10
LastEditors  : 小鹿撞路
Description  : 分析csv
FilePath     : \simple_database\highs_lows.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# 根据数据绘制图形 实参alpha设置透明度，实参facecolor设置填充区颜色
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures -2014\nDeath Valley CA", fontsize=24)
plt.xlabel("", fontsize=6)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()