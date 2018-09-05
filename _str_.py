# -*- coding:utf-8 -*-

#定制类
# __str__类
class Student(object):
    def __init__(self, name):
        self.name = name 
    def __str__(self):
        return "Student object (name: %s)" % self.name

print(Student('Michael'))
# Student('Michael')

# __iter__ 类 

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 #初始化两个计数器a,b

    def __iter__(self):
        return self #实例本身是迭代对象 返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b #计算下一个值
        if self.a > 1000: #退出循环条件
            raise StopIteration()
        return self.a #返回下一个值

for n in Fib():
    print(n)

# __getitem__类 类似list一样能够取出下标元素

class Fib1 (object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a

f = Fib1()
print(f[20])
# print(list(range(5)))

# __getattr__ 获取属性
class Getattr(object):
    def __init__(self):
        self.name = "kk"

    def __getattr__(self,attr):
        if attr == 'score':
            # return 99
            return lambda :99

b = Getattr()
# print(b.score
print(b.score())

# 试试
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    
    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# 属性链式调用
print(Chain().sd.sdd.sddd.sdddd)