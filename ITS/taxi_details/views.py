from django.shortcuts import render
from django.http import HttpResponse
from .forms import TaxiDetailForm
from .models import TaxiDetailPost

# Create your views here.

def form_view(request):
	print TaxiDetailPost.objects.all()
	detail_dictionary = {}
	detail_dictionary["taxi_info"]=TaxiDetailPost.objects.all().order_by("-id")
	return render(request,"taxi_detail.html",detail_dictionary)




