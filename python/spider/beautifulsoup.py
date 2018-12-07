from bs4 import BeautifulSoup
import requests
import re
from urllib import request, parse

url = 'http://www.baidu.com'
#
# rsp = requests.request('get', url)
# print(rsp.text)

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'html5lib')

content = soup.prettify()
# print(content)
# print(soup.head)
# Tag
print(soup.meta)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])

# NavigableString
print(soup.title.string)

# BeautifulSoup
print(type(soup.name))
print(soup.name)
print(soup.attrs)

# contents,children
# for i in soup.style.contents:
#     print(i)

# find_all()
print(soup.find_all('b'))
# 使用正则
'''
for i in soup.find_all(re.compile('^b')):
    print(i)
    
'''

# css选择器
print(soup.select("meta[content='always']"))