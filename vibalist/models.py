from django.db import models

class Item(models.Model):
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
