from urllib import request, parse
from http import cookiejar

cookie = cookiejar.MozillaCookieJar(filename='cookie.txt')

cookie_handler = request.HTTPCookieProcessor(cookie)

http_handler = request.HTTPHandler

https_handler = request.HTTPSHandler

opener = request.build_opener(cookie_handler, http_handler, https_handler)

def savecookie():

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

    # ignore_discard丢弃了也保存
    # ignore_expires过期了也保存
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == '__main__':
    savecookie()