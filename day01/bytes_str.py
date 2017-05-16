#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CC(zizou)
# Email: yyccbbz@l63.com
# pythonstudy--bytes_str
# 2017/5/16 14:31



bytes1 = '€20'.encode('utf-8')
# b'\xe2\x82\xac20'

print(bytes1)

str1 = b'\xe2\x82\xac20'.decode('utf-8')
# '€20'
print(str1)


msg = '我爱北京天安门'
print(msg.encode(encoding='utf-8').decode(encoding='utf-8'))



