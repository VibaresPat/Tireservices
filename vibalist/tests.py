from django.urls import resolve
'''from django.test import TestCase
from vibalist.views import homepage

class HomePageTest(TestCase):

	def test_mainpage_return_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

	 def test_homepage_returns_correct_views(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		string_html = render_to_string('homepage.html')
		self.assertEqual(html, string_html)
		self.assertTemplateUsed(response,'homepage.html')

	def test_root_url_resolve_to_mainpage_view(self)
		found = resolve('/')
		self.assertEqual(found.func, Mainpage)

	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		string_html = render_to_string('homepage.html')
		self.assertEqual(html, string_html)

	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html,strip().startswith('html>'))
		self.assertIn('<title>Contact Tracing List</title', html)
		self.assertTrue(html.strip().endswith('</html>'))
		'''


