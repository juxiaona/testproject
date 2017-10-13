import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib

class BaiDu(unittest.TestCase):
	'''百度搜索'''
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.base_url="http://www.baidu.com"


	def test_search1(self):
		'''搜索关键字selenium'''
		driver=self.driver
		driver.get(self.base_url)
		driver.find_element_by_id("kw").send_keys('selenium')
		driver.find_element_by_id("su").click()

	def test_search2(self):
		'''搜索关键字python'''
		driver=self.driver
		driver.get(self.base_url)
		driver.find_element_by_id("kw").send_keys('python')
		driver.find_element_by_id("su").click()


	def tearDown(self):
		self.driver.close()

def sendmail(filename):


	#发送的附件
	sendfile = open(filename, 'rb').read()
	att = MIMEText(sendfile, 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment; filename="report.html"'
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = Header("自动化测试报告",'utf-8')
	msgRoot.attach(att)

	#发送邮件
	smtp=smtplib.SMTP()
	smtp.connect('smtp.163.com')
	smtp.helo('smtp.163.com')
	smtp.ehlo('smtp.163.com')
	smtp.login('1111', '1111')
	smtp.sendmail('xxxx', 'xxxxx', msgRoot.as_string())
	smtp.quit()




if __name__ == '__main__':
	testunit=unittest.TestSuite()
	testunit.addTest(BaiDu("test_search1"))
	testunit.addTest(BaiDu("test_search2"))
	#按照一定的格式获取当前时间
	now=time.strftime("%Y-%m-%d %H_%M_%S")

	#定义报告存放路径
	filename="./report/"+now+"report.html"
	fp=open(filename,"wb")
	runner=HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况")
	runner.run(testunit)
	fp.close()
	sendmail(filename)
