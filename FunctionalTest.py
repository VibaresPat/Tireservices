from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	
	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Request Form', self.browser.title)

		Vext = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Request Form', Vext)

		Hext = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('-ICT LESSON-', Hext)

		p = self.browser.find_element_by_id('u').text
		self.assertIn('FULLNAME:', p)

		a = self.browser.find_element_by_id('n').text
		self.assertIn('EMAIL:', a)

		t = self.browser.find_element_by_id('a').text
		self.assertIn('DATE:', t)

		p2 = self.browser.find_element_by_id('pangalawa').text
		self.assertIn('COURSE AND SECTION:', p2)

		p3 = self.browser.find_element_by_id('pangatlo').text
		self.assertIn('LESSON:', p3)

		p4 = self.browser.find_element_by_id('pangapat').text
		self.assertIn('REASON:', p4)

		p5 = self.browser.find_element_by_id('panglima').text
		self.assertIn('Note: Provide a formal letter for requesting.', p5)

		form = self.browser.find_element_by_tag_name('form')

		lesson0 = self.browser.find_element_by_name('lesson').click()
		lesson1 = self.browser.find_element_by_name('lesson').click()
		lesson2 = self.browser.find_element_by_name('lesson').click()

		Select1 = self.browser.find_element_by_id('lec').click()
		Select2 = self.browser.find_element_by_id('lab').click()
		Select3 = self.browser.find_element_by_id('all').click()
	

		i= self.browser.find_element_by_id('firstname')  
		self.assertEqual(i.get_attribute('placeholder'),'SN/FN/MN')
		i = self.browser.find_element_by_id('firstname').send_keys("Nice")
		time.sleep(1)

		n= self.browser.find_element_by_id('Gmail')  
		self.assertEqual(n.get_attribute('placeholder'),'@gmail')
		n= self.browser.find_element_by_id('Gmail').send_keys("Nice")
		time.sleep(1)

		u= self.browser.find_element_by_id('birthday') 
		time.sleep(1)

		l= self.browser.find_element_by_id('coursesection')  
		self.assertEqual(l.get_attribute('placeholder'),'Ex: BSIE-ICT-3A')
		l= self.browser.find_element_by_id('coursesection').send_keys("Nice")
		time.sleep(1)

		k= self.browser.find_element_by_id('lec')  
		w= self.browser.find_element_by_id('lab') 
		z= self.browser.find_element_by_id('all') 
		time.sleep(1)

		f= self.browser.find_element_by_id('letter')  
		self.assertEqual(f.get_attribute('placeholder'),'Valid Reason')
		f= self.browser.find_element_by_id('letter').send_keys("Nice")
		time.sleep(1)

		r= self.browser.find_element_by_id('done') 
		time.sleep(1)

		dat = self.browser.find_element_by_id('birthday').click()
		dat = self.browser.find_element_by_id('birthday').send_keys("2012-11-02")
		time.sleep(1)

		sub = self.browser.find_element_by_id('done').click()
		time.sleep(1)


		self.browser.quit()	
		self.browser = webdriver.Firefox()
		self.browser.get('http://localhost:8000')

		lesson0 = self.browser.find_element_by_name('lesson').click()
		lesson1 = self.browser.find_element_by_name('lesson').click()
		lesson2 = self.browser.find_element_by_name('lesson').click()

		Select1 = self.browser.find_element_by_id('lec').click()
		Select2 = self.browser.find_element_by_id('lab').click()
		Select3 = self.browser.find_element_by_id('all').click()
	

		i= self.browser.find_element_by_id('firstname')  
		self.assertEqual(i.get_attribute('placeholder'),'SN/FN/MN')
		i = self.browser.find_element_by_id('firstname').send_keys("Nice")
		time.sleep(1)

		n= self.browser.find_element_by_id('Gmail')  
		self.assertEqual(n.get_attribute('placeholder'),'@gmail')
		n= self.browser.find_element_by_id('Gmail').send_keys("Nice")
		time.sleep(1)

		u= self.browser.find_element_by_id('birthday') 
		time.sleep(1)

		l= self.browser.find_element_by_id('coursesection')  
		self.assertEqual(l.get_attribute('placeholder'),'Ex: BSIE-ICT-3A')
		l= self.browser.find_element_by_id('coursesection').send_keys("Nice")
		time.sleep(1)

		k= self.browser.find_element_by_id('lec')  
		w= self.browser.find_element_by_id('lab') 
		z= self.browser.find_element_by_id('all') 
		time.sleep(1)

		f= self.browser.find_element_by_id('letter')  
		self.assertEqual(f.get_attribute('placeholder'),'Valid Reason')
		f= self.browser.find_element_by_id('letter').send_keys("Nice")
		time.sleep(1)

		r= self.browser.find_element_by_id('done') 
		time.sleep(1)

		dat = self.browser.find_element_by_id('birthday').click()
		dat = self.browser.find_element_by_id('birthday').send_keys("2012-11-02")
		time.sleep(1)

		sub = self.browser.find_element_by_id('done').click()
		time.sleep(1)


		self.browser.quit()	
		


		



		
	


		


if __name__ == '__main__':
	unittest.main()