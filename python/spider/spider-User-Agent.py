'''
    请求header首部行,进行User-Agent设置伪装浏览器
    通过代理服务器进行IP伪装
'''
from urllib import request, parse, error
import chardet
import json

if __name__ == '__main__':

    # 访问地址
    url = 'https://fanyi.baidu.com/sug'
    # 参数设置
    wd = input('请输入:')
    data = {
        'wd':wd
    }
    data = parse.urlencode(data).encode()

    # header设置
    hearde = {
        'Content-Length':len(data),
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    try:
        req = request.Request(url=url, data=data, headers=hearde)
        rsp = request.urlopen(req)
        print(type(rsp))
        rsp = rsp.read()
        cs = chardet.detect(rsp)
        print(cs)
        result = rsp.decode(cs.get('encoding', 'utf-8'))
        result = json.loads(result)

        print(result)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

