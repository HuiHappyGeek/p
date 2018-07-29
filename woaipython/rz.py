# ！ usr/bin/python3 eny
# _*_ coding=utf-8 _*_
__author__='Mark'
__copyright__='Mark'

'''
NOTSET  0
DEBUG  10
INFO   20
WARNING  30
ERROR   40
CRITICAL   50

Loggers
Handles
Filters
Formatters

'''


'''
Logging.Formatter：这个类配置了日志的格式，在里面自定义设置日期和时间，输出日志的时候将会按照设置的格式显示内容。
Logging.Logger：Logger是Logging模块的主体，进行以下三项工作：
1. 为程序提供记录日志的接口
2. 判断日志所处级别，并判断是否要过滤
3. 根据其日志级别将该条日志分发给不同handler

'''
'''
import logging  # 引入logging模块
# 将信息打印到控制台上
logging.basicConfig(level=logging.NOTSET)
logging.debug(u'如果设置了日志级别为NOTSET,那么这里可以采取debug、info的级别的内容也可以显示在控制台上了')
logging.debug(u"苍井空")
logging.info(u"麻生希")
logging.warning(u"小泽玛利亚")
logging.error(u"桃谷绘里香")
logging.critical(u"泷泽萝拉")
'''

'''
import logging  # 引入logging模块
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')
'''
