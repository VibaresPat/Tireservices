from django.urls import path
from . import views



urlpatterns = [
	path('', views.home),
	path('ClientInfo', views.Clientinfos, name="ClientInfo"),
	path('Scheduling', views.sched, name="Scheduling"),
	path('paymentmethod', views.pay, name="paymentmethod"),
	path('reciept', views.nice, name="reciept"),
	path('', views.home),
	path('ApplicantInfo', views.applicants, name="ApplicantInfo"),
	path('details', views.app, name="details"),
	path('Applicantlast', views.last, name="Applicantlast"),
	

]








