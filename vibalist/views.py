from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.
def Lods(request):



	
	if request.method == 'POST':
		
		firstname = request.POST['firstname']
		Gmail = request.POST['Gmail']
		birthday= request.POST['birthday']
		coursesection = request.POST['coursesection']
		letter = request.POST['letter']
		lesson = request.POST['lesson']
		
		
		pat = Item()
		pat.firstname = firstname
		pat.Gmail = Gmail
		pat.birthday = birthday
		pat.coursesection = coursesection
		pat.letter = letter
		pat.lesson = lesson
		pat.save()

	return render (request,'homepage.html')	




def Page(request):
	pat = Item.objects.all().order_by('firstname')
	return render(request,'second.html', {'pat':pat})
	  





	
	

'''from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	#return HttpResponse('homepage')
	return render(request, 'homepage.html')'''

