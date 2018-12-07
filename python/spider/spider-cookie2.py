from urllib import request, parse
from http import cookiejar

# 创建实例
cookie = cookiejar.MozillaCookieJar()

# 读取保存的cookie文件,一处保存多处使用
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)


# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 创建一个https请求管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

# 创建登录函数
# def login():
#     url = 'http://www.renren.com/PLogin.do'
#     email = input('email:')
#     password = input('password:')
#
#     data = {
#         'email': email,
#         'password': password
#     }
#
#     data = parse.urlencode(data)
#
#     # 创建请求对象
#     req = request.Request(url, data=data.encode())
#
#     # 发起请求
#     rsp = opener.open(req)


def getHtml():
    url = 'http://www.renren.com/968991382/profile'

    rsp = opener.open(url)

    html = rsp.read().decode()

    # 把搞到的数据写到一个文件里面
    with open('rspp.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    # login()
    getHtml()