import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱服务器
smtpserver="smtp.163.com"

#发送邮箱用户名和密码
user="jxxxx"
pawd="jxxxxx"

#发送邮箱
sender="x"

#接收邮箱
receiver="xxxx"

#邮件主题
subject="python email test"

#邮箱正文
msg=MIMEText("<html><h1>hello</h1></html>","html","utf-8")
msg['Subject']=Header(subject,'utf-8')

#连接发送邮件
smtp = smtplib.SMTP_SSL()
smtp.connect(smtpserver)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,pawd)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
