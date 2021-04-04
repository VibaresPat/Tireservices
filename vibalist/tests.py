from django.test import resolve
from django.test import TestCase
from vibalist.views import homepage

class HomePageTest(TestCase)

	def test_root_url_resolve_to_mainpage_view(self)
		found = resolve('/')
		self.assertEqual(found.func, homepage)

# Create your tests here.
