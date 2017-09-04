from time import sleep

class BasePage():

	def __init__(self,driver):
		self.driver=driver

	def find_element(self,by,element):
		return self.driver.find_element(by, element)

	def wait_element(self,by,element):
		for i in range(30):
			print(i)
			try:
				element=self.driver.find_element(by,element)
				if element.is_displayed():
					break;
			except:
				pass
			sleep(1)


	def switch_frame(self,element):
		self.driver.switch_to.frame(element)


	def switch_default(self):
		self.driver.switch_to.default_content()

