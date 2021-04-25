from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http:/127.0.0.1:8000')






'''
import unittest

from selenium.webdriver.common.keys import Keys
import time


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

		#Username
		input1 = self.browser.find_element_by_tag_name('p').text
		self.assertIn('USERNAME:', input1)
		firstname = self.browser.find_element_by_id('firstname').send_keys("Patricia")
		time.sleep(2)

		input2 = self.browser.find_element_by_id('lesson').text
		self.assertIn('LECTURE:', input2)

		#lecture
		select = self.browser.find_element_by_id('quantity').send_keys("1")
		time.sleep(2)

		#askme
		input3 = self.browser.find_element_by_id('help').text
		self.assertIn('QUESTION:', input3)
		Baybayin = self.browser.find_element_by_id('baybayin').send_keys("Askme")
		time.sleep(2)
		firstname = self.browser.find_element_by_id('done').click()


if __name__== '__main__':
	unittest.main()	

	browser = webdriver.Firefox()
	browser.get('http://127.0.0.1:8000')

		#H1
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.browser.get('Welcome to Baybayin Project', headerText)

		#Username
		input1 = self.browser.find_element_by_tag_name('p').text
		self.assertIn('USER NAME:', input1)
		firstname = self.browser.find_element_by_id('firstname').send_keys("Patricia")

		#lecture
		input2 = self.browser.find_element_by_tag_name('p').send_keys("1")

		#askme
		input3 = self.browser.find_element_by_tag_name('p').text
		self.assertIn('QUESTION:', input3)
		Baybayin = self.browser.find_element_by_id('baybayin').send_keys("Ask me")
		
		firstname = self.browser.find_element_by_tag_name('done').click()

if __name__== '__main__':
	unittest.main()
		
		#Username
		input1 = self.browser.find_element_by_tag_id('p').text
		self.assertIn('USERNAME:', input1)
		firstname = self.browser.find_element_by_tag_name('firstname').send_keys("Patricia")
		
		#lecture
		input2 = self.browser.find_element_by_id('lesson').text
		self.assertIn('LECTURE:', input2)
		input2 = self.browser.find_element_by_tag_name('h5').send_keys("1")

		#askme
		input3 = self.browser.find_element_by_id('h6').text
		self.assertIn('QUESTION:', input3)
		Baybayin = self.browser.find_element_by_tag_name('baybayin').send_keys("Ask me")
		
		firstname = self.browser.find_element_by_tag_name('done').click()


if __name__== '__main__':
	unittest.main()

		#lecture
		input2 = self.browser.find_element_by_tag_name('lesson').text
		self.assertIn('LECTURE:', input2)

		input4 = self.browser.find_element_by_tag_name('h5').send_keys("1")

		#askme
		input3 = self.browser.find_element_by_id('h6').text
		self.assertIn('QUESTION:', input3)
		Baybayin = self.browser.find_element_by_tag_name('baybayin').send_keys("Ask me")
		
		firstname = self.browser.find_element_by_tag_name('done').click()


if __name__== '__main__':
	unittest.main()

		#askme
		input3 = self.browser.find_element_by_tag_name('p').text
		self.assertIn('QUESTION:', input3)
		Baybayin = self.browser.find_element_by_tag_name('baybayin').send_keys("Ask me")
		
		firstname = self.browser.find_element_by_id('done').click()


if __name__== '__main__':
	unittest.main()	'''


