# Author: CC(zizou)
# Email: yyccbbz@l63.com
# pythonstudy--Homework01
# 2017/5/11 16:15

import getpass

'''
作业一：博客

作业二：编写登陆接口

输入用户名密码
认证成功后显示欢迎信息
输错三次后锁定
 

作业三：多级菜单
三级菜单
可依次选择进入各子菜单
所需新知识点：列表、字典
'''


print("客户您好 欢迎登陆".center(30, '-'))
print('-'*35)
username = input("用户名:")
# password = input("密  码:")
password = getpass.getpass("密  码:")




