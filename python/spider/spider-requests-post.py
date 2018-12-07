
from urllib import request, parse, error
import requests
import chardet
import json

if __name__ == '__main__':

    # 访问地址
    url = 'http://fanyi.baidu.com/sug'
    # 参数设置
    wd = input('请输入:')
    data = {
        'wd':wd
    }
    data = parse.urlencode(data).encode('utf-8')
    # header设置
    hearde = {
        'Content-Length':str(len(data)),
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }

    proxy = {'http': '61.135.217.7:80'}
    try:
        # rsp = requests.post(url, data=data)
        rsp = requests.request('post', url, data=data, proxies=proxy)
        print(type(rsp))
        print(rsp.text)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

