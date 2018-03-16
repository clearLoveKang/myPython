#!/usr/bin/env python3
# -*- coding: utf-8 -*-

index = 0
while index <= 100:
	if index >10:
		break
	print(index)
	index = index+1
print('end')

n = 0
while n<10:
	n = n+1
	if n%2 == 0:
		continue
	print(n)
