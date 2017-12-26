#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 10:10
# @Author  : yc
# @Site    : 
# @File    : Logging.py
# @Software: PyCharm

import logging,time,os,threading
import configRead

# pwd = os.getcwd()  #当前路径

# father_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")  #父路径

# grader_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..") #二级路径
# print(father_path)
# log_path = os.path.join(father_path,"log")
# 路径弄个绝对路径
# log_path = r"E:/studyMenu/PycharmProjects/webAutoTest/log/"

nowTime = time.strftime("%Y%m%d%H%M%S")
result = os.path.join(configRead.sysPath,"result")

if not os.path.exists(result):
    os.mkdir(result)

logPath = os.path.join(result,nowTime)
if not os.path.exists(logPath):
    os.mkdir(logPath)

class Log:

    def __init__(self):
        self.logname = os.path.join(logPath,"out.log")
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(asctime)s]-%(levelname)s:%(message)s')

    def __console(self,level,message):

        # 文件句柄
        fileHandler = logging.FileHandler(self.logname,'a','utf-8')   #'a'为追加模式
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(self.formatter)
        self.logger.addHandler(fileHandler)

        # 流句柄，输出到控制台
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.INFO)
        streamHandler.setFormatter(self.formatter)
        self.logger.addHandler(streamHandler)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        self.logger.removeHandler(fileHandler)
        self.logger.removeHandler(streamHandler)

        fileHandler.close()

    def info(self,message):
        self.__console('info',message)

    def debug(self,message):
        self.__console('debug',message)

    def warning(self,message):
        self.__console('warning',message)

    def error(self,message):
        self.__console('error',message)

class MyLog:
    '''
    Mylog  解决多线程问题
    '''
    log = None
    # 创建互斥锁
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            # 锁定
            MyLog.mutex.acquire()
            MyLog.log = Log()
            # 释放
            MyLog.mutex.release()

        return MyLog.log

# 
# if __name__ == "__main__":
# 
#     log = MyLog.get_log()
# 
#     log.info("测试info")
# 
#     print("555555555555")
# 
#     log.debug("测试debug")
# 
#     log.warning("测试warning")
# 
#     log.error("测试error")