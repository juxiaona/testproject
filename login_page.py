from time import sleep
from selenium.webdriver.common.by import By
from base import BasePage

class MailPage():

	def __init__(self,driver):
		self.driver=driver
		self.base=BasePage(self.driver)

	def login_name(self,username):
		self.base.get_element(By.NAME,'email').clear()
		self.base.get_element(By.NAME,'email').send_keys(username)

	def login_pasw(self,password):
		self.base.get_element(By.NAME,'password').clear()
		self.base.get_element(By.NAME,'password').send_keys(password)

	def login_button(self):
		self.base.get_element(By.ID,'dologin').click()


	def wait_frame(self):
		self.base.wait_element(By.ID,'x-URS-iframe')
			
	def switch_frame(self):
		self.base.switch_frame('x-URS-iframe')

	def switch_default(self):
		self.base.switch_default()




		