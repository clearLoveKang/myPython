# -*- coding:utf-8 -*-

#保留奇数
def is_odd(x):
	return x%2 == 1
	
n = list(filter(is_odd,[1,2,3,4,5,6]))
print(n)

#去除序列中空字符串
def not_empty(s):
	return s and s.strip()
	
p = list(filter(not_empty,['A', '', 'B', None, 'C', '  ']))
print(p)

#过滤出来回数
m = [1,2,3,4,5]
print(m[::-1])

def is_palindrome(n):
	return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#排序sorted
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))

#用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
def by_name(t):
	return t[0]
	
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
	return t[1]
L3 = sorted(L, key=by_score)
print(L3)
