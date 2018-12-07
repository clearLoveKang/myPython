'''
    把cookie作为一个变量打印出来
    看看cookie属性
    name
    value
    domain 可以访问域名
    path
    expires 过期时间
    size
    Http字段
'''
from urllib import request, parse
from http import cookiejar

# 创建一个cookieJar实例
cookie = cookiejar.CookieJar()
# 创建一个cookie处理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建一个http请求处理器
http_handler = request.HTTPHandler()
# 创建一个HTTPS请求处理器
https_handler = request.HTTPSHandler()
# 最后创建请求管理器把需要的处理器都放入处理
opener = request.build_opener(cookie_handler, http_handler, https_handler)

def login():

    url = 'http://www.renren.com/PLogin.do'
    email = input('email:')
    password = input('password:')

    data = {
        'email': email,
        'password': password
    }
    data = parse.urlencode(data)

    req = request.Request(url, data=data.encode())

    rsp = opener.open(req)

if __name__ == '__main__':
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)