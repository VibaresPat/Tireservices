from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path ('admin/',admin.site.urls),
	path('',include('vibalist.urls')),
	]



#luma
'''from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$' ,views.homepage, name='homepage.html'),  
]'''

