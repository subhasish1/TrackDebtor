from django.db import models

class Organisations(models.Model):
	orgname = models.CharField(max_length=50)
	orgemail = models.CharField(max_length=100)
	orgcc  = models.CharField(max_length=500)
	orgsendername = models.CharField(max_length=50)
	orgsenderphn =  models.CharField(max_length=13)
	orgpassword =  models.CharField(max_length=13)
	orglogo = models.ImageField(max_length=150)
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

class Outstanding(models.Model):
	orgid = models.CharField(max_length=3)
	custid = models.CharField(max_length=3)
	bill_no = models.CharField(max_length=20)
	bill_amt = models.CharField(max_length=20)
	due_amt = models.CharField(max_length=10)
	bill_date = models.DateField()
	cleared_on=models.DateField()
	class Meta:
		db_table='outstanding'
		