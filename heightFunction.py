# -*- coding: utf-8 -*-
#切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:3])

List = list(range(100))
print(List)
print(List[0:3]) #L[索引开始:索引结束(不包括当前索引)]
print(List[-10:-1])
print(List[-10:])
print(List[::2])
print(List[:10:2])
#迭代
def findMinAndMax(L):
	if L != []:
		max = L[0]
		min = L[0]
		for i in L:
			if max < i:
				max = i
			if min > i:
				min = i
		return (min, max)
	else:
		return (None, None)
#测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')