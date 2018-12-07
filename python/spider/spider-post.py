# -*- coding:utf-8 -*-
'''
    百度翻译
    使用data
    http://fanyi.baidu.com/sug
    Content-Type: application/json 需要json包
'''
from urllib import request, parse
import json
''' 
    1 利用data构造内容,然后使用urlopen打开
    2 返回一个json格式结果
    3 结果应该是查询的翻译
'''
base_url = 'http://api.mixpace.com/index.php/api/space/getSpaceList'

# kw = input('请输入查询名字:')

data = {}

post_data = parse.urlencode(data)
print(type(post_data), post_data)

post_data = post_data.encode('utf-8')
print(type(post_data), post_data)


rsp = request.urlopen(base_url, data=post_data)

print(rsp.getcode())
# 读取返回信息后先解码
rsp = rsp.read().decode()

# 解码后吧数据还原成json
rsp = json.loads(rsp)
print(type(rsp), rsp)

for k in rsp:
    print(k, '...', rsp[k])

for v in rsp.values():
    print(v)
    for item in v:
        print(item)
        for k,v in item.items():
            print(k, '---', v)



