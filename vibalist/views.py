from django.shortcuts import redirect, render
from .models import ClientInfo, Scheduling, Payment, Paymentmethod, ApplicantInfo, ApplicantDetails, ApplicantTransfer


def home(request):

	return render(request,'home.html')

def Clientinfos(request):

	return render(request,'ClientInfo.html')
	
def sched(request):
	
	client=ClientInfo.objects.create(
		Childname = request.POST['Childname'],
		Guardianname = request.POST['Guardianname'],
		Age = request.POST['Age'],
		Cellphone = request.POST['Cellphone'],
		Location = request.POST['Location'],
		mail = request.POST['mail'],
	)

	return render(request,'Scheduling.html')

def pay(request):

	scd = Scheduling.objects.create(
		Date = request.POST['Date'],
		Subject1 = request.POST['Subject1'],
		Schedule = request.POST['Schedule'],
		Time =  request.POST['Time'],
		Message = request.POST['Message'],	
		select = request.POST['select'],
		place = request.POST['tot_pin_requested'],	
		TransportationAmount= request.POST['TransportationAmount'],
	)
	
	return render(request,'paymentmethod.html')


def nice(request):

	bayad = Payment.objects.create(
		Quantity = request.POST['Quantity'],
		TOTAL = request.POST['TOTAL'],
		Quantity1 = request.POST['Quantity1'],
		TOTAL2 = request.POST['TOTAL2'],

	)
 
	bayad2 = Paymentmethod.objects.create(
 		selectsss = request.POST['selectsss'],
 		Holder = request.POST['Holder'], 
		Bank = request.POST['Bank'],
		Account = request.POST['Account'],
		Routing = request.POST['Routing'],
		payment = request.POST['payment'],
		Amount = request.POST['Amount'],
		card = request.POST['card'],
		Expiry = request.POST['Expiry'],
		code = request.POST['code'],
		zips = request.POST['zips'],
 	)

	return render(request,'reciept.html')

def home(request):

	return render(request,'home.html')


def applicants(request):

	return render(request,'ApplicantInfo.html')

def app(request):

	method = ApplicantInfo.objects.create(
		applicant = request.POST['applicant'],
		last = request.POST['last'],
		email = request.POST['email'],
		cell = request.POST['cell'],
		ress = request.POST['ress'],
		zipss = request.POST['zipss'],
	)

	return render(request, 'details.html')


def last(request):

	dtls= ApplicantDetails.objects.create(
		grad = request.POST['grad'],
		schools = request.POST['schools'],
		maj = request.POST['maj'],
		deg = request.POST['deg'],
		taon = request.POST['taon'],
		schl = request.POST['schl'],
		jor = request.POST['jor'],
		ree = request.POST['ree'],
		yea = request.POST['yea'],
		award = request.POST['award'],
		avail = request.POST['avail'],
		hayts = request.POST['hayts'],
		oras = request.POST['oras'],
		teach = request.POST['teach'],
	)


	return render(request, 'Applicantlast.html')







	






































































