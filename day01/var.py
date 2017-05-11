#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CC
# Email: yyccbbz@l63.com


# print("Hello World!!!")
#
#
# name = input("What is your name?")
# print("Hello " + name)
#
#
# username = input("username: ")
# password = input("password:　")
# print(username,password)

name = input("name : ")
age = int(input("age : ")) #integer
print(type(age))
job = input("job : ")
salary = input("salary : ")

#字符串格式化输出：

info = '''
--------info of %s----------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (name, name, age, job, salary)

print(info)

info2 = '''
--------info of {_name}----------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)

print(info2)

info3 = '''
--------info of {0}----------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)

print(info3)



