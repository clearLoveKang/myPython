'''
    python 正则是re
    re.compile(正则表达式) 这是一个pattern
    使用pattern方法和规则对文本进行匹配,匹配结果是一个Match对象
    使用Match的方法对结果进行操作
'''
import re

# 写一个表达式
s = r'\d+'
pattern = re.compile(s)
m = pattern.match('rr123456rerrw', 2, 5)
print(m)
print(m.group())
print(m.start(0))
print(m.end(0))
print(m.span())