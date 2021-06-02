from django.shortcuts import redirect, render
from .models import Customer,Admin,Home,InputLog,Seconddisplay,ThirdDisplay,FourthPrice,fifthAppointment,AnimHomeservices

# from .models import User, Info

def una(request):

	return render(request,'una.html')

def PatPat(request):

	Admin=Walk.objects.create(
		Walk = request.POST['COOSE'],
		invent = request.POST['CHOO'],
		)

	Customer=Appoint.objects.create(
		sched = request.POST['CHSE'],
		
		)
	Home=Home.objects.create(
		home = request.POST['CHOO'],
					
		)	
	return redirect('Call')
	
def Vibaaaaa(request):

	return render(request,'panglima.html')


def panglima(request):

	return render(request,'panglima.html')

def chhuuyyy(request):
	AnimHomeservices = anim.objects.create(
		Name = request.POS['Name'],
		CP = request.POST ['CP'],
		Add = request.POST ['Add'],
		arawngpunta =request.POST['arawngpunta'],
		Orasngpunta =request.POST['Orasngpunta'],
		sasakyan =request.POST['sasakyan']
		)

	return redirect('next')

def chhhayy(request):
	return render(request,'pangatlo.html')









	








































































'''# Create your views here.
def Lods(request):



	
	if request.method == 'POST':


		ict = User.objects.create()
		Item.objects.create(
			firstname = request.POST['firstname'],
			Gmail= request.POST['Gmail'], 
			birthday = request.POST['birthday'],
			coursesection = request.POST['coursesection'], 
			letter = request.POST['letter'],
			lesson = request.POST['lesson'],
			)
		return redirect('vibbsss')
		
		
		pat = Item()
		pat.firstname = firstname
		pat.Gmail = Gmail
		pat.birthday = birthday
		pat.coursesection = coursesection
		pat.letter = letter
		pat.lesson = lesson
		pat.save()

	return render (request,'una.html')	




def Page(request):
	pat = Item.objects.all().order_by('firstname')
	return render(request,'second.html', {'pat':pat})
	  





	
	

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	#return HttpResponse('homepage')
	return render(request, 'homepage.html')'''


