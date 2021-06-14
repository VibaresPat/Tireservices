from django.urls import path
from . import views



urlpatterns = [
	path('', views.home),
	path('ClientInfo.html', views.Clientinfos, name="ClientInfo.html"),
	path('Scheduling.html', views.sched, name="Scheduling.html"),
	path('paymentmethod.html', views.pay, name="paymentmethod.html"),
	path('home.html', views.nice, name="home.html"),
	path('ApplicantInfo.html', views.applicant, name="ApplicantInfo.html"),
	path('details.html', views.app, name="details.html"),
	path('Applicantlast.html', views.last, name="Applicantlast.html"),
	
	









	# path('vibbsss', views.PatPat, name="vibbsss"),
	# path('Call', views.Vibaaaaa, name="Call"),

	
	# path('', views.panglima),
	# path('vibbsss', views.chhuuyyy, name="vibbsss"),
	# path('next', views.chhhayy, name="next"),
	
	#vibbsss
]








