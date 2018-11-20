# 练习
# 将所有级别日志写入磁盘文件
# all.log 文件记录所有日志信息 格式为时间- 级别- 日志信息
# error.log文件记录error信息,格式为 时间-级别- 文件名[:行号]-日志信息
# all.log 每天凌晨进行日志切割


import logging
import logging.handlers
import datetime

# 定义一个all.log的logger
logger = logging.getLogger('mylogger')
# 设置级别
logger.setLevel(logging.DEBUG)



# 设置all.log日志处理器
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight',interval=1, backupCount=7, encoding=None, delay=False, utc=False, atTime=None)
# 设置all.log的输出格式
rf_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))



# 定义一个error.log的logger
sf_handler = logging.FileHandler('error.log')
# 设置记录级别
sf_handler.setLevel(logging.ERROR)
# 格式化文件
sf_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s'))

# 把相应的处理器装到logger
logger.addHandler(rf_handler)
logger.addHandler(sf_handler)

logger.debug('这是debug级别日志')
logger.info('这是info级别日志')
logger.warning('这是warning级别日志')
logger.error('这是error级别日志')
logger.critical('这是critical级别日志')