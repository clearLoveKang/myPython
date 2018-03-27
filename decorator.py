# -*- coding: utf-8 -*-

def now():
	print('2018-03-21')

f = now
f()
#本质上，decorator(装饰器)就是一个返回函数的高阶函数。

def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def nnow():
	print('2018-03-21')
nnow()

import time,functools
#练习
def metric(fn):
	@functools.wraps(fn)
	def _wrapper(*args, **kw):
		start_time = time.time()
		result = fn(*args, **kw)
		end_time = time.time()
		print('%s executed in %s ms' % (fn.__name__, (end_time - start_time)))
		return result
	return _wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
	






