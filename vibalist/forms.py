from django import forms
from .models import Scheduling

class labas(forms.ModelForm):
	class Meta:
		model = Scheduling
		fields = "__all__"























