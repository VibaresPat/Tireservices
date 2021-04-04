from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

''' browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')'''

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Baybayin Project', self.browser.title)

		#H1
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Welcome to Baybayin Project', headerText)
		time.sleep(2)

		#askme
		input1 = self.browser.find_element_by_tag_name('p').text
		self.assertIn('USERNAME:', input1)
		firstname = self.browser.find_element_by_id('firstname').send_keys("Patricia")
		time.sleep(2)

		input2 = self.browser.find_element_by_id('we').text
		self.assertIn('LECTURE:', input2)

		#lecture
		select = self.browser.find_element_by_id('quantity').send_keys("1")
		time.sleep(2)


		input3 = self.browser.find_element_by_id('wew').text
		self.assertIn('QUESTION:', input3)
		Baybayin = self.browser.find_element_by_id('baybayin').send_keys("Askme")
		time.sleep(2)

		firstname = self.browser.find_element_by_id('ediw').click()



		
		


if __name__== '__main__':
	unittest.main()	
