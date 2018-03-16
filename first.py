#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = input('请输入你的名字')
print('hello,', name)
print('浮点数',10e2)
print('转译符号','I\'m \"ok\"')
print(r'\\\多行转译\\')
print('换\n行')
print('''超级
...换
...行''')
print('布尔型：',3>2,2>3)
print('运算符and',True and True ,True and False, False and False)
print('运算符or',True or True, True or False, False or False)
print('运算符not', not True, not False, not 1>2)
print('hi%s,you have $%d. 100%%' %('老表',1000))
