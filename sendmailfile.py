import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#发送邮箱服务器
smtpserver="smtp.163.com"

#发送邮箱用户名和密码
user="ju_xiaona@163.com"
pawd="jxn461028"

#发送邮箱
sender="ju_xiaona@163.com"

#接收邮箱
receiver="ju_xiaona@163.com"

#邮件主题
subject="python email test"

#发送的附件
sendfile = open('D:/testproject/report/report.html', 'rb').read()
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="report.html"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

#连接发送邮件
smtp = smtplib.SMTP_SSL()
smtp.connect(smtpserver)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,pawd)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
