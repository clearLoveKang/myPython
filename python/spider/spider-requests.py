import requests

url = 'https://wx.dxs6.cn/api/xiaohua/upload/min_img/20180918/201809189fxSpDRUad.jpg'

# rsp = requests.get(url)
# print(rsp.text)
# rsp = requests.request('get', url)
# print(rsp.text)

# 带参数的
# data = {
#     'wd': '红烧肉'
# }
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

rsp = requests.get(url, headers=headers)

# requests 自动获取cookie 获取方便使用随意
cookiejar = rsp.cookies
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiedict)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)