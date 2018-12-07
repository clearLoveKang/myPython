from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
# 得到网站页面
driver.get('http://www.baidu.com')

text = driver.find_element_by_id('wrapper').text
print(text)

print(driver.title)
# 对页面进行截图屏幕快照
driver.save_screenshot('title.png')

# 获取输入框 输入东西
driver.find_element_by_id('kw').send_keys(u'大熊猫')

# 输入后点击查找按钮
driver.find_element_by_id('su').click()
time.sleep(5)
driver.save_screenshot('panda.png')

# 把当前页面cookie得到
print(driver.get_cookies())

# 模拟按键 全选 剪切
driver.find_element_by_id('kw').send_keys(Keys.COMMAND, 'a')
driver.find_element_by_id('kw').send_keys(Keys.COMMAND, 'x')

# 输入框空了 再输入点东西试试
driver.find_element_by_id('kw').send_keys(u'航空母舰')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.save_screenshot('hangmu.png')

# 清空也可以clear不用那么麻烦
driver.find_element_by_id('kw').clear()

# 最后退出浏览
driver.quit()





