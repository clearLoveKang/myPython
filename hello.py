#!/usr/bin/env python3
# -*- coding utf-8 -*-

'a test module'

__author__ = 'kang'

import sys

def test():
	args = sys.argv
	print(args)
	if len(args)==1:
		print('Hello,World')
	elif len(args)==2:
		print('Hello, %s' % args[1])
	else:
		print('Too many arguments')
		
if __name__ == '__main__':
	test()

def _private_1(name):
	print('Hello, %s' % name)

def _private_2(name):
	print('hi, %s' % name)

def greeting(name):
	if len(name)>2:
		return _private_1(name)
	else:
		return _private_2(name)

