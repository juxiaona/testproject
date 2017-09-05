from base import Base
import unittest
from selenium import webdriver
from time import sleep

class BaiduSet(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.base=Base(self.driver)
		self.base.open("http://www.baidu.com")
		self.base.max_window()

	def test_setting(self):
		self.base.move_to_element("link_text=>设置")
		self.base.click_element("link_text=>搜索设置")
		self.base.select_element('id=>nr', '50')
		self.base.click_element('class=>prefpanelgo')

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()

