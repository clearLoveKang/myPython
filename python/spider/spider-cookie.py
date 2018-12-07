
from urllib import request, parse, error
from http import cookiejar
import chardet
import json

if __name__ == '__main__':

    # # 创建cookiejar实例
    # cookie = cookiejar.CookieJar()
    # # 创建一个cookie管理器
    # cookie_handler = request.HTTPCookieProcessor(cookie)
    # # 创建http请求管理器
    # http_handler = request.HTTPHandler()
    # # 创建一个https请求管理器
    # https_handler = request.HTTPSHandler()



    # 访问地址
    url = 'http://www.renren.com/968991382/profile'

    hearde = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Cookie': 'anonymid=jp3tnb6dm6f8rf; depovince=SH; _r01_=1; JSESSIONID=abcYhQZeSM5ZzbpfX7JDw; ick_login=4d7cfb7e-df1b-4294-933e-760d88d23839; ick=53b265c8-9511-4bf9-a862-60f9253c1025; wp_fold=0; jebecookies=45223245-dc73-4365-9c26-5940b4a2d92e|||||; _de=F73C2752110EEBCA6D5D4E9A6EE4D047; p=86a93d713c89871d8829cfa36b10c1ce2; first_login_flag=1; ln_uact=13253521216; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=ba7869c81d73a2a30371a64bcdd7dae02; societyguester=ba7869c81d73a2a30371a64bcdd7dae02; id=968991382; xnsid=8e163199; ver=7.0; loginfrom=null; jebe_key=3f943314-e748-41b2-8f76-1559173b37a2%7C89d84ce4628b0b5d46c451010b5e5784%7C1543804408479%7C1%7C1543804408651'
    }
    try:
        req = request.Request(url, headers=hearde)
        rsp = request.urlopen(req)
        print(type(rsp))
        rsp = rsp.read()
        result = rsp.decode()
        print(result)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

