#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CC(zizou)
# Email: yyccbbz@l63.com
# pythonstudy--list_tuple
# 2017/5/16 14:39

import copy

names = ["Alex", "Tenglan", "Eric", "Rain", "Tom", "Amy"]

a = names[1:4]  # 取下标1至下标4之间的数字，包括1，不包括4
print("a = ", a)
print(type(a))

b = names[1:-1]  # 取下标1至-1的值，不包括-1
print("b = ", b)

c = names[0:3]
print("c = ", c)

d = names[:3]  # 如果是从头开始取，0可以忽略，跟上句效果一样
print("d = ", d)

e = names[3:]  # 如果想取最后一个，必须不能写-1，只能这么写
print("e = ", e)

f = names[3:-1]  # 这样-1就不会被包含了
print("f = ", f)

g = names[0::2]  # 后面的2是代表，每隔一个元素，就取一个
print("g = ", g)

h = names[::2]  # 和上句效果一样
print("h = ", h)

names.append("我是新来的")
names.insert(2,"强行从Eric前面插入")
names[3] = "该换人了"
names.pop() #删除列表最后一个值

names.index("Amy")

print(names)
names.sort()
print(names)


names2 = copy.deepcopy(names)
print(names2)