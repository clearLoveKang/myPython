# -*- coding: utf-8 -*-
#高阶函数map / reduce
def f(x):
	return x*x

m = map(f,[1,2,3,4,5])
print(list(m))

#求和
print(sum([1,2,3,4,5]))
from functools import reduce
def add(x,y):
	return x+y
d = reduce(add,[1,2,3,4,5])
print(d)

#变成整数1234
def oInt(x,y):
	return x*10+y
s = reduce(oInt,[1,2,3,4])
print(s)

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字.

def normalize(name):
   return name.title()
# 测试: capitalize() title()把第一个字母转化为大写字母，其余小写
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
#把字符串'123.456'转换成浮点数123.456：
def str2float(s):
	n = s.index('.')
	list1 =list(map(int,[x for x in s[:n]]))
	list2 = list(map(int,[x for x in s[n+1:]]))
	def oInt(x,y):
		return x*10+y
	return reduce(oInt,list1)+reduce(oInt,list2)/10**len(list2)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
