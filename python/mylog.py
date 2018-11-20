# -*- coding:utf-8 -*-
# 变量 重复使用的一个量,或者叫代号
#命名规则:1可包含数字,大小写字母,下划线或者更多,但是我么不推荐出前三者之外的东西咯
#        2:数字不可以开头,一般以下划线开头有特殊含义不推荐
#        3:大小写敏感 推荐使用固定含义的英文或者缩写,驼峰命名法(大驼峰 类命名)(小驼峰 普通变量或函数)
#保留字关键字注意


#设置总的basicConfig

import logging

LOG_FORMAT = "%(asctime)s===%(levelname)s++++++%(message)s"

#设置总的日志配置
logging.basicConfig(filename='mylog.log', level=logging.DEBUG, format=LOG_FORMAT)
logging.debug('这是debug级别日志')
logging.info('这是info级别日志')
logging.warning('这是warning级别日志')
logging.error('这是error级别日志')
logging.critical('这是critical级别日志')
# 使用log总控制
logging.log(logging.DEBUG,'这是debug级别日志')
logging.log(logging.INFO,'这是info级别日志')
logging.log(logging.WARNING,'这是warning级别日志')
logging.log(logging.ERROR,'这是error级别日志')
logging.log(logging.CRITICAL,'这是critical级别日志')