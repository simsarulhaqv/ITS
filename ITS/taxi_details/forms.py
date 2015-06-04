from django import forms
from .models import TaxiDetailPost

class TaxiDetailForm(forms.ModelForm):
	class Meta:
		model = TaxiDetailPost
		fields = ["name","taxi_id","aadhar_no","age","sex"]

