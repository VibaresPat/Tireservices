from django.shortcuts import redirect, render
from .models import ClientInfo, Scheduling, Payment, Paymentmethod, ApplicantInfo, ApplicantDetails, ApplicantTransfer
# from .models import User, Info

def home(request):

	return render(request,'home.html')

def Clientinfos(request):

	# Admin=Walk.objects.create(
	# 	Walk = request.POST['COOSE'],
	# 	invent = request.POST['CHOO'],
	# 	)

	# Customer=Appoint.objects.create(
	# 	sched = request.POST['CHSE'],
		
	# 	)
	# Home=Home.objects.create(
	# 	home = request.POST['CHOO'],
					
	# 	)	
	return render(request,'ClientInfo.html')
	
def sched(request):
	# Admin=Walk.objects.create(
	# 	Walk = request.POST['COOSE'],
	# 	invent = request.POST['CHOO'],
	# 	)

	# Customer=Appoint.objects.create(
	# 	sched = request.POST['CHSE'],
		
	# 	)
	# Home=Home.objects.create(
	# 	home = request.POST['CHOO'],
					
	# 	)
	return render(request,'Scheduling.html')

def pay(request):
	# Admin=Walk.objects.create(
	# 	Walk = request.POST['COOSE'],
	# 	invent = request.POST['CHOO'],
	# 	)

	# Customer=Appoint.objects.create(
	# 	sched = request.POST['CHSE'],
		
	# 	)
	# Home=Home.objects.create(
	# 	home = request.POST['CHOO'],
					
	# 	)
	return render(request,'paymentmethod.html')


def nice(request):

	return render(request,'home.html')


	

def applicant(request):

	return render(request,'ApplicantInfo.html')




def app(request):

	return render(request, 'details.html')


def last(request):

	return render(request, 'Applicantlast.html')







	








































































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


