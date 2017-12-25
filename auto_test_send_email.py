#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 16:32
# @Author  : yc
# @Site    : 
# @File    : auto_test_send_email.py
# @Software: PyCharm

import os
import smtplib
import unittest
import time
import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import codecs

def send_mail(file_name):
    '''发送邮件'''
    msg = MIMEMultipart()

    #发件人
    sender = '260936767@qq.com'
    #收件人
    receiver = 'yangchao@cevlink.com'
    #邮件主题
    header = '自动化测试报告-'+time.strftime("%Y-%m-%d")
    msg['Subject'] = Header(header,'utf-8')

    #正文
    text = MIMEText(_text=u'邮件自动发送，请勿回复。',_subtype='plain',_charset='utf-8')
    msg.attach(text)

    #附件
    f = open(file_name,'rb')
    mail_body = f.read()
    f.close()
    # 截取最后文件名
    file_name_new = file_name.split("\\")[-1]
    print(file_name_new)
    # text1 = MIMEText(_text=mail_body, _subtype='html', _charset='utf-8')
    # msg.attach(text1)


    att = MIMEText(mail_body, _subtype='html',_charset="utf-8")
    att["Content-Type"] = 'application/octet-stream'

    att['Content-Disposition'] = 'attachment;filename = %s' %file_name_new
    msg.attach(att)

    #发送邮件
    host = 'smtp.qq.com'
    port = 465
    username = '260936767@qq.com'
    password = 'kggpekpwcotjbgfj'
    try:
        smtp = smtplib.SMTP_SSL(host=host,port=port)
        smtp.connect(host=host,port=port)
        smtp.set_debuglevel(1)
        smtp.login(user=username,password=password)
        smtp.sendmail(from_addr=sender,to_addrs=receiver,msg=msg.as_string())
        smtp.quit()
    except Exception as e:
        print(str(e))


def  send_report(testreport):
    '''
    查找最新报告，发送报告
    :param testreport:
    :return:
    '''
    result_dir = testreport
    lists =os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getctime(result_dir+"\\"+fn))
    file_name = os.path.join(result_dir,lists[-1])
    print(file_name)
    send_mail(file_name)

def createsuite():
    testunit = unittest.TestSuite()
    case_path = os.path.join(os.getcwd(), "testCase")
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern='test*.py',
                                                   top_level_dir=None)
    for test_case in discover:
        print(test_case)
        testunit.addTests(test_case)
    return testunit

if __name__ == "__main__":
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    report_path = os.path.join(os.getcwd(), "report")
    file_name = report_path+"/result "+now_time+".html"
    fp = open(file_name,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title=u"测试标题",
                                           description=u"描述")
    all_testCase = createsuite()
    runner.run(all_testCase)
    fp.close()
    send_report(report_path)