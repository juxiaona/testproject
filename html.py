import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time

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