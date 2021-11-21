#!/usr/bin/env python
# coding=utf-8
'''
Author       : 小鹿撞路
Date         : 2021-09-25 13:43:47
LastEditTime : 2021-09-25 14:52:01
LastEditors  : 小鹿撞路
Description  : 猜数字
FilePath     : \python_study\guess_number.py
self_motto   : 倘若自己都不为自己活出自己的人生，那还有谁会为自己而活呢。
'''
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess!')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break  # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my answer in '+str(guessesTaken)+' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
