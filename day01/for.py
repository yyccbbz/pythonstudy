#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CC(zizou)
# Email: yyccbbz@l63.com
# pythonstudy--for
# 2017/5/11 14:11



'''
count = 0
while True:
    print("你是风儿我是沙,缠缠绵绵到天涯...", count)
    count += 1
    if count == 100:
        print("去你妈的风和沙,你们这些脱了裤子是人,穿上裤子是鬼的臭男人..")
        break
'''


for i in range(0, 10, 1):
    if i < 3:
        print("loop:", i)
    else:
        continue    # 跳出本次循环，继续下次循环
    print("hehe.....")


