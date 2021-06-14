from django.contrib import admin
from .models import ClientInfo, Scheduling, Payment, Paymentmethod, ApplicantInfo, ApplicantDetails, ApplicantTransfer
#Register your models here.
admin.site.register(ClientInfo)
admin.site.register(Scheduling)
admin.site.register(Payment)
admin.site.register(Paymentmethod)
admin.site.register(ApplicantInfo)
admin.site.register(ApplicantDetails)
admin.site.register(ApplicantTransfer)


