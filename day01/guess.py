#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CC(zizou)
# Email: yyccbbz@l63.com
# pythonstudy--guess
# 2017/5/10 17:55


# input 默认字符串

age_of_oldboy = 56
tries = 0
guess_age = 0

while tries < 3:
    guess_age = int(input("guess age: "))
    if guess_age > age_of_oldboy:
        print("think smaller...")
    elif guess_age < age_of_oldboy:
        print("think bigger!!!")
    elif guess_age == age_of_oldboy:
        print("yes, you got it !!!!!")
        break
    tries = tries + 1
    if tries == 3:
        continue_confirm = input("do you want to keep guessing..?")
        if continue_confirm != 'n':
            tries = 0
# else:
#     print("Sorry!!! you have no tries!")

# for tries in range(3):
#     guess_age = int(input("guess age: "))
#     if guess_age > age_of_oldboy:
#         print("think smaller...")
#     elif guess_age < age_of_oldboy:
#         print("think bigger!!!")
#     elif guess_age == age_of_oldboy:
#         print("yes, you got it !!!!!")
#         break
# else:
#     print("Sorry!!! you have no tries!")

