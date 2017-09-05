from base import Base

class LoginPage():

	def __init__(self,driver):

		self.driver=driver
		self.base=Base(self.driver)

	def login_name(self,username):

		self.base.clear_element("name=>email")
		self.base.sendkeys("name=>email",username)

	def login_pasw(self,password):

		self.base.clear_element('name=>password')
		self.base.sendkeys('name=>password',password)

	def login_button(self):

		self.base.click_element('id=>dologin')
			
	def switch_frame(self):

		self.base.switch_frame('id=>x-URS-iframe')

	def switch_frame_out(self):
		self.base.switch_frame_out()




		