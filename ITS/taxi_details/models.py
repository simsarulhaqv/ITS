from django.db import models
from add_taxi.models import Taxi

# Create your models here.

class TaxiDetailPost(models.Model):
	name = models.CharField(max_length=30)
	taxi_id = models.CharField(max_length=10)
	aadhar_no = models.CharField(max_length=40)
	age = models.IntegerField()
	sex = models.CharField(max_length=6)

	def __unicode__(self):
		return self.name

