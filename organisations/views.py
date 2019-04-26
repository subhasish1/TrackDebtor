from django.shortcuts import render
from django.conf.urls.static import static
from .models import Organisations , Customer,Outstanding

# Create your views here.

def index(request):
    return render(request,'organisations/index.html')
def portfolio(request):
    return render(request,'organisations/portfolio.html')
def orgreg(request):
	if request.method == 'POST':
		
		org_name=request.POST.get('orgname')
		org_email=request.POST.get('orgemail')
		org_cc=request.POST.get('orgcc')
		org_sender_email=request.POST.get('orgsenderemail')
		org_sender_phn=request.POST.get('orgsenderphn')
		org_password=request.POST.get('orgpassword')
		
		c = Organisations(orgname = org_name,orgemail = org_email, orgcc=org_cc,orgsendername=org_sender_email, orgsenderphn=org_sender_phn, orgpassword=org_password)
		c.save()
		return render(request,'organisations/orgRegister.html')
	else:

		return render(request,'organisations/orgRegister.html')
def custreg(request):
	if request.method == 'POST':
		
		org_id=request.POST.get('orgid')
		cust_name=request.POST.get('custname')
		cust_email=request.POST.get('custemail')
		cust_phn=request.POST.get('custphone')
		cust_status=request.POST.get('custstatus')

		cust = Customer(orgid=org_id, custname=cust_name, custemail=cust_email,custphn=cust_phn,custstatus=cust_status )
		cust.save()
		return render(request,'organisations/orgRegister.html')
	else:
		return render(request,'organisations/customer.html')
def outstanding(request,orgid):
	if request.method == 'POST':
		
		org_id=request.POST.get('orgid')
		cust_id=request.POST.get('custid')
		bill_no=request.POST.get('bill_no')
		bill_amt=request.POST.get('bill_amt')
		due_amt=request.POST.get('due_amt')
		bill_date=request.POST.get('bill_date')
		cleared_on=request.POST.get('cleared_on')

		p = outstanding(orgid=org_id, custid=cust_id, bill_no=bill_no, bill_amt=bill_amt, due_amt=due_amt, bill_date=bill_date, cleared_on=cleared_on )
		p.save()
		return render(request,'organisations/outstanding.html')
	else:
		return render(request,'organisations/outstanding.html')