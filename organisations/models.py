from django.db import models

class Organisations(models.Model):
	orgname = models.CharField(max_length=50)
	orgemail = models.CharField(max_length=100)
	orgcc  = models.CharField(max_length=500)
	orgsendername = models.CharField(max_length=50)
	orgsenderphn =  models.CharField(max_length=13)
	orgpassword =  models.CharField(max_length=13)
class Meta:
		db_table='organisations'

class Customer(models.Model):
	orgid = models.CharField(max_length=3)
	custname = models.CharField(max_length=50)
	custemail = models.CharField(max_length=100)
	custphn = models.CharField(max_length=13)
	custstatus = models.CharField(max_length=10)
class Meta:
	db_table='customer'
