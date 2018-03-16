# -*- coding: utf-8 -*-

def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

print(fact(5))
#print(fact(1000))

def hanoi(n,a,b,c):
	if n == 1:
		print(a,'-->',c)
	else:
		hanoi(n-1,a,c,b)
		hanoi(1,a,b,c)
		hanoi(n-1,b,a,c)
n = int(input("请输入汉诺塔的层数："))
hanoi(n,"A","B","C")
