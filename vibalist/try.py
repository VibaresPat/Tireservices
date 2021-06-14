from django.db import models

class ClientInfo(models.Model):
	

	#clientInfo
	Childname =models.CharField(max_length=10, default='none')
	Guardianname =models.CharField(max_length=10, default='none')
	Age =models.CharField(max_length=10, default='none')
	Cellphone =models.CharField(max_length=10, default='none')
	Location =models.CharField(max_length=10, default='none')
	mail =models.CharField(max_length=10, default='none')

	def __str__(self):
		return self.Childname 




	#scheduling
class Scheduling(models.Model):

	Date =models.DateTimeField(null=True)
	Subject1 =models.CharField(max_length=10, default='none')
	Schedule =models.CharField(max_length=10, default='none')
	Time = models.TimeField(null=True)
	Message =models.TextField(max_length=2000, default='none')

	choices =(('selecthome', 'Home Visiting'), ('selectonline', 'Online'), ('selecthouse', 'Teacher House'))
	sltss =models.CharField(max_length=25, choices=choices, default='none')

	picka =(('min', 'Mindanao'), ('vis', 'Visayas'), ('luz', 'Luzon'), ('metro', 'Metro Manila'))
	place =models.CharField(max_length=25, choices=picka, default='none')

	Transportation_Amount=models.CharField(max_length=10, default='none')
	
	def __str__(self):
		return self.Date


class Payment(models.Model):

	Quantity =models.IntegerField(null=True)
	TOTAL =models.IntegerField(null=True)
	Quantity1 =models.IntegerField(null=True)
	TOTAL2 = models.TimeField(null=True)

	def __str__(self):
		return self.Quantity


class Paymentmethod(models.Model):


	choice =(('selectmethod', 'BANK ACCOUNT'), ('slctmthd', 'GCASH'), ('slectmthod', 'CREDIT CARD'))
	selectsss =models.CharField(max_length=25, choices=choice, default='none')

	Holder =models.CharField(max_length=10, default='none')
	Bank =models.CharField(max_length=10, default='none')
	Account =models.CharField(max_length=10, default='none')
	Routing =models.CharField(max_length=10, default='none')
	payment =models.CharField(max_length=10, default='none')
	Amount =models.CharField(max_length=10, default='none')
	card =models.CharField(max_length=10, default='none')
	Expiry =models.CharField(max_length=10, default='none')
	code =models.CharField(max_length=10, default='none')
	zips =models.CharField(max_length=10, default='none')

	def __str__(self):
		return self.selectsss

class ApplicantInfo(models.Model):

	applicant =models.CharField(max_length=10, default='none')
	last =models.CharField(max_length=10, default='none')
	email =models.CharField(max_length=10, default='none')
	cell =models.CharField(max_length=10, default='none')
	ress =models.CharField(max_length=10, default='none')
	zipss =models.CharField(max_length=10, default='none')

	def __str__(self):
		return self.applicant 

class ApplicantDetails(models.Model):


	choices =(('selectmethod', 'BANK ACCOUNT'), ('slctmthd', 'GCASH'), ('slectmthod', 'CREDIT CARD'))
	grad =models.CharField(max_length=25, choices=choices, default='none')

	schools =models.CharField(max_length=10, default='none')
	maj =models.CharField(max_length=10, default='none')
	deg =models.CharField(max_length=10, default='none')
	taon =models.CharField(max_length=10, default='none')
	schl =models.CharField(max_length=10, default='none')
	jor =models.CharField(max_length=10, default='none')
	ree =models.CharField(max_length=10, default='none')
	yea =models.CharField(max_length=10, default='none')
	award =models.CharField(max_length=10, default='none')
	avail =models.CharField(max_length=10, default='none')
	hayts =models.CharField(max_length=10, default='none')
	oras =models.CharField(max_length=10, default='none')
	teach =models.CharField(max_length=10, default='none')

	def __str__(self):
		return self.grad

class ApplicantTransfer(models.Model):


	chooseee =(('yes', 'Yes'), ('no', 'No'))
	que =models.CharField(max_length=10, choices=chooseee, default='none')

	pick=(('salary', 'Gcash'), ('slry', 'Bank Account'), ('sltss', 'Credit Card'))
	Transfering =models.CharField(max_length=25, choices=pick, default='none')


	gcashh =models.CharField(max_length=10, default='none')
	hold =models.CharField(max_length=10, default='none')
	carddy =models.CharField(max_length=10, default='none')
	bankyy =models.CharField(max_length=10, default='none')
	acc =models.CharField(max_length=10, default='none')
	nice =models.CharField(max_length=10, default='none')

	def __str__(self):
		return self.que



















	






class Customer(models.Model):
	

	#main
	Appoint =models.CharField(max_length=10, default='none')

	def __str__(self):
		return self.Appoint


class Admin(models.Model):
	Walk =models.CharField(max_length=10, default='none')
	invent =models.CharField(max_length=10, default='none')
	

	def __str__(self):
		return self.Walk 

class Home(models.Model):
	Services =models.CharField(max_length=10, default='none')


	def __str__(self):
		return self.Services

class InputLog(models.Model):
	second = models.ForeignKey(Admin, default=None, on_delete=models.CASCADE, null=True)
	#nameofadmin
	Log = models.CharField(max_length=20, null=True)
	#passwordofadmin
	Pass = models.CharField(max_length=20, null=True)


	def __str__(self):
		return self.Log

class Seconddisplay(models.Model):
	seconds = models.ForeignKey(Admin, default=None, on_delete=models.CASCADE, null=True)
	#nameofclient
	firstname = models.CharField(max_length=20, null=True)
	#DATE
	birthday = models.DateTimeField(null=True)
	#wheels
	kotse =(('tr', '6 Wheels Up'), ('ca', '4 Wheels'), ('ja', '3 Wheels'),('mo', '2 Wheels'))
	Vehicle =models.CharField(max_length=10, choices=kotse, default='none')

	def __str__(self):
		return self.firstname


class fifthAppointment(models.Model):

	fifth =  models.ManyToManyField(Customer)
	Client = models.CharField(max_length=20, null=True)
	Contact = models.CharField(max_length=20, null=True)
	#DATE
	dateofsched = models.DateTimeField(null=True)
	#time
	timeofsched = models.DateTimeField(null=True)

	kot =(('six', '6 Wheels Up'), ('four', 'four Wheels'), ('three', '3 Wheels'),('two', '2 Wheels'))
	pangbyahe =models.CharField(max_length=10, choices=kot, default='none')

	def __str__(self):
		return self.Client



class AnimHomeservices(models.Model):

	anim =models.ManyToManyField(Home)

	Name = models.CharField(max_length=20, null=True)
	CP = models.CharField(max_length=20, null=True)
	Add = models.CharField(max_length=20, null=True)
	#DATE
	arawngpunta = models.DateTimeField(null=True)
	#time
	Orasngpunta = models.DateTimeField(null=True)

	se =(('hay', '6 Wheels Up'), ('hey', 'four Wheels'), ('hiy', '3 Wheels'),('hoy', '2 Wheels'))
	sasakyan =models.CharField(max_length=10, choices=se, default='none')

	def __str__(self):
		return self.Name

	
class ThirdDisplay(models.Model):
	papa =  models.ForeignKey(Admin, default=None, on_delete=models.CASCADE, null=True)
	home =  models.ManyToManyField(Home)
	Appointme =  models.ManyToManyField(Customer)

	Issue = models.CharField(max_length=20, null=True)
	VehiclesIssue_choices = ( ('None', 'None'), ('Vehicle1', 'Interior Tire Repair'), ('vehicle2', 'Radiator Overhaul'), ('vehicle3', 'Welding'), ('vehicle4', 'Jack Repair'), ('vehicle5', 'Tire Repair'), ('vehicle6', 'Interior') )
	select = models.CharField(max_length=50, choices=VehiclesIssue_choices, null=True)
	select = models.CharField(max_length=50, choices=VehiclesIssue_choices, null=True)
	select = models.CharField(max_length=50, choices=VehiclesIssue_choices, null=True)
	select = models.CharField(max_length=50, choices=VehiclesIssue_choices, null=True)
	select = models.CharField(max_length=50, choices=VehiclesIssue_choices, null=True)
	select = models.CharField(max_length=50, choices=VehiclesIssue_choices, null=True)


	def __str__(self):
		return self.Issue


class FourthPrice(models.Model):

	pap1 =  models.ForeignKey(Admin, default=None, on_delete=models.CASCADE, null=True)
	home1 =  models.ManyToManyField(Home)
	Appointme1 =  models.ManyToManyField(Customer)

	itr = models.CharField(max_length=20, null=True)
	ro =models.CharField(max_length=20, null=True)
	wg =models.CharField(max_length=20, null=True)
	jr =models.CharField(max_length=20, null=True)
	it =models.CharField(max_length=20, null=True)
	Quants1 = models.CharField(max_length=20, null=True)
	Quants2 = models.CharField(max_length=20, null=True)
	Quants3 = models.CharField(max_length=20, null=True)
	Quants4 = models.CharField(max_length=20, null=True)
	Quants5 = models.CharField(max_length=20, null=True)
	Quants6 =models.CharField(max_length=20, null=True)
	ttl = models.IntegerField(null=True)


	def __str__(self):
		return self.itr



































































































'''class Item(models.Model):


	ict = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)


	#FULLNAME
	firstname = models.CharField(max_length=20, null=True)
	#Email
	Gmail = models.CharField(max_length=20, null=True)
	#DATE
	birthday = models.DateTimeField(null=True)
	#Course and Section
	coursesection = models.CharField(max_length=20, null=True)
	#lesson
	pick=(('lec', 'LECTURE'),('lab','LABARATORY'),('all','BOTH'))
	lesson = models.CharField(max_length=10, choices=pick, default='none')
	#Reason
	letter = models.TextField(max_length=1000, null=True)




	def __str__(self):
		return self.firstname

'''
