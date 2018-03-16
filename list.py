# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
# 测试:列表生成式
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

#斐波那契数列 generator 生成器
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = (b, a+b)
		n = n + 1
	return "done"
print(fib(6))

for n in fib(6):
	print(n)

#杨辉三角 generator 生成器
def triangles():
	N = [1]
	while True: 
		yield N[:]
		N.append(0)
		N = [N[i-1]+N[i] for i in range(len(N))]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print(results)		
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')