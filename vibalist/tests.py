from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from vibalist.views import Lods
from django.urls import resolve
from vibalist.models import Item, User
from django.urls import reverse



class IndexTest(TestCase):

	def html_index_root_homepage_na_gawa_ko(self):
		found = resolve('/')
		self.assertEqual(found.func, Lods)

		
	def test_index_returns_correct_view(self):
		request = HttpRequest()
		response = Lods(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'homepage.html')
		self.assertIn('<title>Request Form</title>', html)

		self.assertTemplateUsed(response, 'homepage.html')
		self.assertIn('<html>', html)
		self.assertIn('<head>', html)
		self.assertIn('<title>Request Form</title>', html)
		self.assertIn('</head>', html)
		self.assertIn('<body style="background-color:  #fff7e6">', html)
		self.assertIn('<center>', html)
		self.assertIn('<h1 style="color:#805500; font-family: sans-serif; font-size: 50px; background-color:  #f2ffcc">Request Form</h1>', html)
		self.assertIn('<h2 style="color:#4d3300;font-family: courier;font-size: 30px; ">-ICT LESSON-</h2>',html)
		self.assertIn('<p id="u">FULLNAME:</p>', html)
		self.assertIn('<input type="text" id="firstname" name="firstname" placeholder="SN/FN/MN" required>', html)
		self.assertIn('<p id="n">EMAIL:</p>', html)
		self.assertIn(' <input type="text" id="Gmail" name="Gmail" placeholder="@gmail"required>', html)
		self.assertIn('<p id="a">DATE:</p>', html)
		self.assertIn('<input type = "date" id="birthday" name="birthday" required>', html)
		self.assertIn('<p id="pangalawa">COURSE AND SECTION:</p>', html)
		self.assertIn('<input type="text" id="coursesection" name="coursesection" placeholder="Ex: BSIE-ICT-3A"required>', html)
		self.assertIn('<div id="lesson">', html)
		self.assertIn('<p id="pangatlo">LESSON:</p>', html)
		self.assertIn('<input type ="radio" id="lec" name="lesson" value="LECTURE" required>LECTURE', html)
		self.assertIn('<input type ="radio" id="lab" name="lesson" value="LABARATORY" required>LABARATORY', html)
		self.assertIn('<input type ="radio" id="all" name="lesson" value="BOTH" required>BOTH', html)
		self.assertIn('<p id="pangapat">REASON:</p>', html)
		self.assertIn('<p id="panglima">Note: Provide a formal letter for requesting.</p>', html)
		self.assertIn('<input type="text" size ="50" id="letter" name="letter" placeholder ="Valid Reason"required>', html)
		self.assertIn('<input type="Submit" id=done value="Submit">', html)
		self.assertIn('<br>', html)
		self.assertIn('</center>', html)
		self.assertIn('</body>', html)
		self.assertIn('</html>', html)
	
		self.assertTrue(html.strip().endswith('</html>'))


class ORM_Patricia_Vibs(TestCase):
	def test_mo_here(self):
		Item1 = Item()
		Item1.firstname = 'Vibares, Patricia M.'
		Item1.save()
		Item2 = Item()
		Item2.Gmail = 'vibarespatricia@gmail.com'
		Item2.save()
		Item3 = Item()
		Item3.birthday = '2021-11-04' 
		Item3.save()
		Item4 = Item()
		Item4.coursesection = 'BSIE-ICT-3A'
		Item4.save()
		Item5 = Item()
		Item5.lesson = 'BOTH'
		Item5.save()
		Item6 = Item()
		Item6.lesson = 'Fever'
		Item6.save()
		saveall = Item.objects.all()

		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		
		self.assertEqual(Item1.firstname, 'Vibares, Patricia M.')
		self.assertEqual(Item2.Gmail, 'vibarespatricia@gmail.com')
		self.assertEqual(Item3.birthday, '2021-11-04')
		self.assertEqual(Item4.coursesection, 'BSIE-ICT-3A')
		self.assertEqual(Item5.lesson, 'BOTH')
		self.assertEqual(Item6.lesson, 'Fever')


class ORM_Vibssss_Pat(TestCase):
	def test_another_test_mo_here(self):
		Item1 = Item()
		Item1.firstname = 'Vibares, Patricia M.'
		Item1.save()
		Item2 = Item()
		Item2.Gmail = 'vibarespatricia@gmail.com'
		Item2.save()
		Item3 = Item()
		Item3.birthday = '2021-11-04' 
		Item3.save()
		Item4 = Item()
		Item4.coursesection = 'BSIE-ICT-3A'
		Item4.save()
		Item5 = Item()
		Item5.lesson = 'BOTH'
		Item5.save()
		Item6 = Item()
		Item6.letter = 'Fever'
		Item6.save()
		
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		
		self.assertEqual(Item1.firstname, 'Vibares, Patricia M.')
		self.assertEqual(Item2.Gmail, 'vibarespatricia@gmail.com')
		self.assertEqual(Item3.birthday, '2021-11-04')
		self.assertEqual(Item4.coursesection, 'BSIE-ICT-3A')
		self.assertEqual(Item5.lesson, 'BOTH')
		self.assertEqual(Item6.letter, 'Fever')

#try lang kung gagana cheat ko buburahin ko din. 
class ORM_Vibs_chay(TestCase):
	def test_third_test_mo_here(self):
		Item1 = Item()
		Item1.firstname = 'Vibares, Patricia M.'
		Item1.save()
		Item2 = Item()
		Item2.Gmail = 'vibarespatricia@gmail.com'
		Item2.save()
		Item3 = Item()
		Item3.birthday = '2021-11-04' 
		Item3.save()
		Item4 = Item()
		Item4.coursesection = 'BSIE-ICT-3A'
		Item4.save()
		Item5 = Item()
		Item5.lesson = 'BOTH'
		Item5.save()
		Item6 = Item()
		Item6.letter = 'Fever'
		Item6.save()
		
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		
		self.assertEqual(Item1.firstname, 'Vibares, Patricia M.')
		self.assertEqual(Item2.Gmail, 'vibarespatricia@gmail.com')
		self.assertEqual(Item3.birthday, '2021-11-04')
		self.assertEqual(Item4.coursesection, 'BSIE-ICT-3A')
		self.assertEqual(Item5.lesson, 'BOTH')
		self.assertEqual(Item6.letter, 'Fever')

class Views(TestCase):
	def test_vi_ba(self):
		Item.objects.create(firstname='firstname', 
			Gmail='Gmail', birthday='birthday',
			coursesection='coursesection',lesson='lesson', letter='letter' )
		response = self.client.get('/app/views.Lods/')
	

class ListViewTest(TestCase):

	def test_uses_list_template(self):
		ict = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

	def test_uses_home_template(self):
		response = self.client.get('/vibbsss/')
		self.assertTemplateUsed(response, 'second.html')

	def test_displays_all_list_items(self):
		ict = User.objects.create()
		firstname = Item.objects.create(firstname='firstname')
		Gmail = Item.objects.create(Gmail='Gmail')
		birthday = Item.objects.create(birthday='2012-11-02')
		coursesection = Item.objects.create(coursesection='coursesection')
		lesson = Item.objects.create(lesson='lesson')
		letter = Item.objects.create(letter='letter')
		response = self.client.get('/')

		self.assertIn('firstname', response.content.decode())
		self.assertIn('Gmail', response.content.decode())
		self.assertIn('birthday', response.content.decode())
		self.assertIn('coursesection', response.content.decode())
		self.assertIn('lesson', response.content.decode())
		self.assertIn('letter', response.content.decode())

		firstname = Item.objects.get(firstname="firstname")
		Gmail = Item.objects.get(Gmail="Gmail")
		birthday = Item.objects.get(birthday="2012-11-02")
		coursesection = Item.objects.get(coursesection="coursesection")
		lesson = Item.objects.get(lesson="lesson")
		letter = Item.objects.get(letter="letter")
		self.assertEqual(Item.objects.count(), 6)

		
class Views(TestCase):
	def setUp(self):
		firstname = Item.objects.create()
		Gmail = Item.objects.create()
		birthday = Item.objects.create()
		coursesection = Item.objects.create()
		lesson = Item.objects.create()
		letter = Item.objects.create()
		
		Item.objects.create(
			firstname = 'Vibares, Patricia M.',
			Gmail = 'vibarespatricia@gmail.com',
			birthday = '2012-11-02',
			coursesection = 'BSIE-ICT-3A',
			lesson = 'BOTH',
			letter = 'Fever',
			)
		self.client.post('/vibbsss/', name='Vibares, Patricia M.')
		
		response = self.client.post('/vibbsss/')

		self.assertEqual(Item.objects.count(), 7)
		#self.assertRedirects(response, '/vibbsss/')

	def test_redirect_view(self):
		firstname = Item.objects.get(firstname="Vibares, Patricia M.")
		Gmail = Item.objects.get(Gmail="vibarespatricia@gmail.com")
		birthday = Item.objects.get(birthday="2012-11-02")
		coursesection = Item.objects.get(coursesection="BSIE-ICT-3A")
		lesson = Item.objects.get(lesson="BOTH")
		letter = Item.objects.get(letter="Fever")

		response = self.client.post('/vibbsss/')
		#self.assertRedirects(response, '/vibbsss/')


class Models(TestCase):

	def models(self, 
		ict="test1", 
		firstname="test2", 
		Gmail="test3", 
		birthday="test4", 
		coursesection="test5", 
		lesson="test6", 
		letter="test7"):
		
		return User.objects.create()
		return Item.objects.create(
			ict="ict", 
			firstname="firstname", 
			Gmail="Gmail", 
			birthday="birthday", 
			coursesection="coursesection", 
			lesson="lesson", 
			letter="letter", )

	def test_chuchay_now(self):
		chuchay = self.models()
		self.assertTrue(isinstance(chuchay, User))
		self.assertFalse(isinstance(chuchay, Item))


#feeling ko ito yung di mabilang sa unittest pero isosolve ko sa susunod na araw
class URL(TestCase):

	def urls(self):
		found = resolve()
		self.assertEqual(found.func, homepage)
		self.assertEqual(found.func, vibbsss)

		url = reverse('homepage')
		self.assertEqual(resolve(url).func, homepage)

		url = reverse('vibbsss')
		self.assertEqual(resolve(url).func, vibbsss)

'''