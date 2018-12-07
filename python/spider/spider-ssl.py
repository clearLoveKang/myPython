from urllib import request
import ssl
'''
    12306竟然加入了ssl协议
    不管他了,如果碰见有安全层问题的网站
    需要建立ssl环境搞一下
'''
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.12306.cn/mormhweb/'

rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)