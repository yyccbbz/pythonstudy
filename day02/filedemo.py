#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CC(zizou)
# Email: yyccbbz@l63.com
# pythonstudy--filedemo
# 2017/5/11 16:56

# 打开文件
f = open('lyrics')
# 读一行
first_line = f.readline()
print('first line:', first_line)

print('我是分隔线'.center(50, '-'))

# 读取剩下的所有内容,文件大时不要用
data = f.read()
# 打印文件
print(data)

# 关闭文件
f.close()
