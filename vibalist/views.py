from django.shortcuts import redirect, render
from .forms import labas
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
		# place = request.POST['tot_pin_requested'],	
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

	display = ClientInfo.objects.last
	display1 = Scheduling.objects.last
	display2 = Payment.objects.last
	display3 = Paymentmethod.objects.last

	return render(request, 'reciept.html', {
		'display': display,
		'display1': display1,
		'display2': display2,
		'display3': display3,}

	)



def dlet(request):

	display = ClientInfo.objects.last
	display1 = Scheduling.objects.last
	display2 = Payment.objects.last
	display3 = Paymentmethod.objects.last

	return render(request, 'reciept.html',{
		'display': display,
		'display1': display1,
		'display2': display2,
		'display3': display3,}

	)

def edit(request,id):
	display1 = Scheduling.objects.get(id=id)
	return render(request, 'edit.html', {'display1':display1})

def update(request, id):
	display1 = Scheduling.objects.get(id=id)
	form = labas(request.POST, instance = display1)
	if form.is_valid():
		form.save()
	return redirect("/tanggalin")

	return render(request, 'edit.html', {'display1': display1})

def destroy(request,id):

	display1 = Scheduling.objects.get(id=id)
	display1.delete()
	return redirect("/tanggalin")



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

def finallast(request):

	huli= ApplicantTransfer.objects.create(

		Transfering = request.POST['Transfering'],
		gcashh = request.POST['gcashh'],
		hold = request.POST['hold'],
		carddy = request.POST['carddy'],
		bankyy = request.POST['bankyy'],
		acc = request.POST['acc'],
		nice = request.POST['nice'],
	)

	display4 = ApplicantInfo.objects.last
	display5 = ApplicantDetails.objects.last
	

	return render(request, 'receipt2.html', {
		'display4': display4,
		'display5': display5,}

	)

	return render(request, 'receipt2.html')

























































# def alisin(request):

# 	display1 = ApplicantDetails.objects.last

# 	return render(request, 'receipt2.html',{
# 		'display5' : display5,}

# 	)
# def alisin2(request,id):
	
# 	display1 = ApplicantDetails.objects.get(id=id)
# 	display1.delete()
# 	return redirect("/alis")
	





# def updateScheduling(request, pk):

# 	viba = Scheduling.objects.get(id=pk)
# 	form = SchedulingForm(instance=viba)

# 	if request.method == 'POST':
# 		form = SchedulingForm(request.POST, instance=viba)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'update.html', context)

# def deleteScheduling(request, pk):
# 	viba = Scheduling.objects.get(id=pk)
# 	if request.method == "POST":
# 		viba.delete()
# 		return redirect('/')

# 	context = {'item':viba}
# 	return render(request, 'delete.html', context)






	






































































