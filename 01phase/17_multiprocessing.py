#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/17 17:19
# @Author  : yc
# @Site    : 
# @File    : 17_multiprocessing.py
# @Software: PyCharm

'''多进程 实现并发'''

# from time import time,sleep,ctime
# import  multiprocessing
#
# def super_player(fileName,time):
#     for i in range(2):
#         print(u"开始播放：%s,开始时间：%s" %(fileName,ctime()))
#         sleep(time)
#
# list = {'过火.mp3':3,'战狼II.mp4':5}
#
# threads = []
# files = range(len(list))
#
# print(files)
#
# for fileName,time in list.items():
#     #创建线程 已进程来创建
#     t = multiprocessing.Process(target=super_player,args=(fileName,time))
#     threads.append(t)
#
# if __name__ =="__main__":
#
#     for i in files:
#         threads[i].start()
#
#     for i in files:
#         threads[i].join()
#
#     print("end")


'''pipe  &&  Queue'''

# import  multiprocessing
# # from multiprocessing import Connection
# # import os,time
#
# pipe = multiprocessing.Pipe()
#
# def proc1(pipe):
#     pipe.Send('hello')
#     print('proc1 rec:'pipe.recv())
#
# def proc2(pipe):
#     pipe.Send('hello,too')
#     print('proc2 rec:'pipe.recv())
#
# p1 = multiprocessing.Process(target=proc1,args=(pipe[0],))
# p2 = multiprocessing.Process(target=proc1,args=(pipe[1],))
#
#
# p1.start()
# p2.start()
# p1.join()
# p2.join()



