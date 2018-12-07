

from selenium import webdriver
import time

# 通过Keys模拟键盘
from selenium.webdriver.common.keys import Keys

# 操作那个浏览器就创建那个实例
#executable_path='/Users/apple/phantomjs/bin/phantomjs'
dirver = webdriver.PhantomJS(executable_path='/Applications/phantomjs/bin/phantomjs')

dirver.get('http://www.baidu.com')
time.sleep(3)
# 查找一下标签

print('Title:{0}'.format(dirver.title))