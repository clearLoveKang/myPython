

from urllib import request, parse
import chardet

if __name__ == '__main__':
    base_url= 'http://www.baidu.com/s?'

    wd = input('Input your keywords')

    qs = {
        'wd':wd
    }
    qs = parse.urlencode(qs)
    print(qs)
    fullurl = base_url + qs
    print(fullurl)
    # 03打开相应的url并把页面返回
    rsp = request.urlopen(fullurl)
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