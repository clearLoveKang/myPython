# -*- coding:utf-8 -*-

# metaclass是类的末班,所以必须从type类型派生
class ListMeatclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return tyoe.__new__(cls, name, bases, attrs)