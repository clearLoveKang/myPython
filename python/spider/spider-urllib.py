

from urllib import request
import chardet

if __name__ == '__main__':
    url= 'http://www.mixpace.com.cn'

    # 03打开相应的url并把页面返回
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)
    '''
        geturl 
        info 也就是返回 http头部信息
        getcode
    '''
    print('URL:{0}'.format(rsp.geturl()))
    print('INFO:{0}'.format(rsp.info()))
    print('GETCODE:{0}'.format(rsp.getcode()))



    # 01读取出来的数据为bytes
    html = rsp.read()
    print(type(html))

    # 02利用第三方包chardet检测编码格式
    cs = chardet.detect(html)
    print(cs)


    html = html.decode(cs.get('encoding','utf-8'))
    print(html)