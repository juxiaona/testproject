
class BaiduPage():
	
	def __init__(self,driver):
		self.driver=driver

	def input_text(self,search_text):
		self.driver.find_element_by_id("kw").send_keys(search_text)

	def button_click(self):
		self.driver.find_element_by_id('su').click()