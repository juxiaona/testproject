from time import sleep
from selenium.webdriver.common.by import By
from base_page import BasePage

class MailPage():

	def __init__(self,driver):
		self.driver=driver
		self.base=BasePage(self.driver)

	def login_name(self,username):
		self.base.location(By.NAME,'email').clear()
		self.base.location(By.NAME,'email').send_keys(username)

	def login_pasw(self,password):
		self.base.location(By.NAME,'password').clear()
		self.base.location(By.NAME,'password').send_keys(password)

	def login_button(self):
		self.base.location(By.ID,'dologin').click()


	def wait_frame(self):
		self.base.wait_element(By.ID,'x-URS-iframe')
			
	def switch_frame(self):
		self.base.switch_frame('x-URS-iframe')

	def switch_default(self):
		self.base.switch_default()




		