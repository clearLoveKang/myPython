# -*- coding: utf-8 -*-
# -*- ax2+bx+c=0 -*-
import math

def quadratic(a, b, c):
	if b*b-4*a*c > 0 or b*b-4*a*c == 0:
		x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
		x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
		return x1,x2
	else:
		return '无解'

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(1,2,1))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

def power(x,n):
	s = 1
	while n>0:
		s = s*x
		n = n-1
	return s
print(power(2,2))
