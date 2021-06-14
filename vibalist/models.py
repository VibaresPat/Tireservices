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



	

