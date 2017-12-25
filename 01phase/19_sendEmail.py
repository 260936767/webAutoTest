#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 10:55
# @Author  : yc
# @Site    : 
# @File    : 19_sendEmail.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText  #邮件正文
from email.mime.multipart import MIMEMultipart  #带附件
from email.header import Header  #邮件标题

# sender = "yangchao@cevlink.com"
# receiver = "260936767@qq.com"
sender = "260936767@qq.com"
receiver = "yangchao@cevlink.com"
subject = "python email test"

# smtpserver = "smtp.exmail.qq.com"
smtpserver = "smtp.qq.com"
# username = "yangchao@cevlink.com"
# password = "ZDWL@yc123"
username = "260936767@qq.com"
password = "kggpekpwcotjbgfj"  #QQ邮箱授权码


# msg = MIMEText('<html><h1>hello</h1></html>','html','utf-8')

# msg = MIMEMultipart('related')
msg = MIMEMultipart()

#标题
msg['Subject'] = Header(subject,'utf-8')

############# 读取附件部分 ###############
f = open(r'E:/studyMenu/PycharmProjects/webAutoTest/report/report2017-08-13_10_48_49.html','rb')
mail_body = f.read()
f.close()

############# 添加附件部分 ###############
# att = MIMEText(mail_body,_subtype='html',_charset='utf-8')
att = MIMEText(mail_body,_subtype='html',_charset = 'utf-8')
att["Content-Type"] = 'application/octet-stream'

#附件，文件名
att['Content-Disposition'] = 'attachment;filename = "report2017-08-13_10_48_49.html"'
msg.attach(att)  #附件


############# 发送邮件部分 ###############

# smtp = smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
#smtp的发送服务，端口
smtp = smtplib.SMTP_SSL(smtpserver,465)
# smtp = smtplib.SMTP()
# smtp.connect()
smtp.set_debuglevel(1)
smtp.login(username,password)
smtp.sendmail(from_addr=sender,to_addrs=receiver,msg=msg.as_string())
smtp.quit()

