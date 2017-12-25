#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 15:51
# @Author  : yc
# @Site    : 
# @File    : 17_threading.py
# @Software: PyCharm

'''多线程 threading '''

# 对于python而言，由于其使用了全局解释锁(GIL)，所以python的多线程并不能实现并发。
# 因此，python的并发是通过多进程来实现的！！！
# 然后，很自然你就会思考了，进程之间不共享资源，实现通信就会麻烦一些咯，
# 不过好在multiprocessing内提供了很多进程间通信的接口，包括管道pipe，队列queue等。
# 对于更大型的项目，我们部署到多台服务器上运行的话，机器间通信会更麻烦一些，
# 不过也有很多并行框架，很经典的celery之类的。
# 而且远程主机间通信业有很多方式，比如使用消息队列实现通信的kafka
# IPC(进程间通信)

# from threading import Thread
# import threading
# from time import sleep,ctime
#
# def loop0():
#     print("loop0 开始的时间 ",ctime())
#
#     sleep(4)
#
#     print("loop0 结束的时间 ",ctime())
#
# def main():
#     print("程序开始的时间 ",ctime())
#
#     threading._start_new_thread(loop0,())
#     print("程序结束的时间 ",ctime())
#
# if __name__ =="__main__":
#     main()
#
# import threading
#
# # 创建自己的线程类
# class MyThread(threading.Thread):
#     def __init__(self,name = None):
#         threading.Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         print(self.name)
#
#
# def test():
#     for i in range(0,100):
#         t = MyThread("thread_"+str(i))
#         t.run()
#
# if __name__ =="__main__":
#     test()


from time import sleep,ctime
import threading  #支持守护线程

def music(name):
    for i in range(5):
        print(U"我在听%s 音乐 %s" %(name,ctime()))
        sleep(3)

def move(name):
    for i in range(5):
        print(U"我在看 %s 电影 %s" %(name,ctime()))
        sleep(5)

# 创建线程数组 装载线程
threads = []
# threading.Thread来创建线程
t1 = threading.Thread(target=music,args=(u"过火",))
# 线程加入数组
threads.append(t1)

t2 = threading.Thread(target=move,args=(u"战狼II",))
threads.append(t2)





if __name__ == "__main__":

# 单线程
    # print(u"开始 %s" %ctime())
    # music(u"music")
    # move(u"move")
    # print(u"结束 %s" %ctime())

    # 开启线程
    for i in threads:
        i.start()
    # 守护线程   等待线程终止
    for i in threads:
        i.join()

    print(u"结束 %s" %ctime())