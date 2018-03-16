# -*- coding: utf-8 -*-
#Iterable 可迭代的
#Iterator 迭代器

#一般for循环
for x in [1,2,3,4,5]:
	print(x)

#等价下边迭代器
#首先定义一个Iterator对象
it = iter([1,2,3,4,5])
#循环
while True:
	try:
		#获得下一个值
		x = next(it)
		print(x)
	except StopIteration:
		break

