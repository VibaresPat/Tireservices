from django.urls import path
from . import views



urlpatterns = [
	path('', views.home, name="home"),
	path('ClientInfo', views.Clientinfos, name="ClientInfo"),
	path('Scheduling', views.sched, name="Scheduling"),
	path('paymentmethod', views.pay, name="paymentmethod"),
	path('reciept', views.nice, name="reciept"),
	path('tanggalin', views.dlet, name="tanggalin"),
	path('edit/<int:id>', views.edit),
	path('update/<int:id>', views.update),
	path('delete/<int:id>', views.destroy),



	path('', views.home),
	path('ApplicantInfo', views.applicants, name="ApplicantInfo"),
	path('details', views.app, name="details"),
	path('Applicantlast', views.last, name="Applicantlast"),
	path('receipt2', views.finallast, name="receipt2"),




	
]


	# path('alis', views.alisin, name="alis"),
	# path('delete/<int:id>', views.alisin2),
	# path('update_Scheduling/<str:pk>/', views.updateScheduling, name="update_Scheduling"),
	# path('delete_Scheduling/<str:pk>/', views.deleteScheduling, name="delete_Scheduling"),





