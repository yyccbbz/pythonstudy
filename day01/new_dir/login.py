#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CC(zizou)
# Email: yyccbbz@l63.com
# pythonstudy--login
# 2017/5/15 12:10


import getpass

# 使用密文，导入模块

_username = "zizou"
_password = "abc123"

username = input("username: ")
password = input("password:　")
# password = getpass.getpass("password:　")

if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")


print(username, password)







