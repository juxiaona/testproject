from selenium import webdriver
from time import sleep
import unittest
from login_page import MailPage
from selenium.webdriver.common.by import By

class Maillogin(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("http://mail.163.com")

	def test_login(self):
		mail=MailPage(self.driver)
		mail.wait_frame()
		mail.switch_frame()
		mail.login_name('ju_xiaona')
		mail.login_pasw('jxn0124')
		mail.login_button()
		mail.switch_default()
		
		sleep(3)


	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()









