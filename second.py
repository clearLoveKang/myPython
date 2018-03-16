#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tuple = ('神哥','蛋蛋','肥宇')
print(tuple[1])
list = ['one','two','three']
list.append('four')
print(list)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi<18.5:
	print('体重过轻')
elif 18.5<bmi<=25:
	print('正常')
elif 25<bmi<=28:
	print('过重')
elif 28<bmi<=32:
	print('肥胖')
else :
	print('严重肥胖')

sum = 0
for x in list(range(101)):
	sum = sum+x
	print(sum)

