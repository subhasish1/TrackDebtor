from django.db import models

class organisations(models.Model):
	orgid = models.CharField(max_length=3)
	orgname = models.CharField(max_length=50)
	orgemail = models.CharField(max_length=100)
	orgcc  = models.CharField(max_length=500)
	orgsendername = models.CharField(max_length=50)
	orgsenderphn =  models.CharField(max_length=13)
