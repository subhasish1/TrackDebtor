from django.shortcuts import render
from django.conf.urls.static import static
from .models import Organisations , Customer,Outstanding
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'organisations/index.html')
def portfolio(request):
    return render(request,'organisations/portfolio.html')

def handle_uploaded_file1(f):  
    with open('organisations/static/organisations/images/'+f.org_name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def orgreg(request):
    if request.method == 'POST':
        
        org_name=request.POST.get('orgname')
        org_email=request.POST.get('orgemail')
        org_cc=request.POST.get('orgcc')
        org_sender_email=request.POST.get('orgsenderemail')
        org_sender_phn=request.POST.get('orgsenderphn')
        org_password=request.POST.get('orgpassword')
        orglogo=request.POST.get('orglogo')
        
        c=Organisations(orgname = org_name,orgemail = org_email,orgcc=org_cc,orgsendername=org_sender_email,orgsenderphn=org_sender_phn,orgpassword=org_password,orglogo=orglogo)
        c.save()
        handle_uploaded_file1(request.FILES['orglogo'])
        return HttpResponse(request.FILES['orglogo'].org_name)
        #return render(request,'organisations/orgRegister.html')
       # return HttpResponse(request.FILES['picture'].name)
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
def outstanding(request):
    if request.method == 'POST':
        
        org_id=request.POST.get('orgid')
        cust_id=request.POST.get('custid')
        bill_no=request.POST.get('bill_no')
        bill_amt=request.POST.get('bill_amt')
        due_amt=request.POST.get('due_amt')
        bill_date=request.POST.get('bill_date')
        cleared_on=request.POST.get('cleared_on')

        p = Outstanding(orgid=org_id, custid=cust_id, bill_no=bill_no, bill_amt=bill_amt, due_amt=due_amt, bill_date=bill_date, cleared_on=cleared_on )
        p.save()
        return render(request,'organisations/outstanding.html')
    else:
        return render(request,'organisations/outstanding.html')