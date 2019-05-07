from django.shortcuts import render, redirect
from django.conf.urls.static import static
from .models import Organisations , Customer,Outstanding
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from organisations.forms import CustomerForm
from apscheduler.schedulers.background import BackgroundScheduler



def index(request):
    return render(request,'organisations/index.html')
def portfolio(request):
    return render(request,'organisations/portfolio.html')

def handle_uploaded_file1(f):  
    with open('organisations/static/organisations/images/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def orgreg(request):
    if request.method == 'POST':
        
        org_name=request.POST.get('orgname')
        org_email=request.POST.get('orgemail')
        org_cc=request.POST.get('orgcc')
        org_sender_email=request.POST.get('orgsendermail')
        org_sender_phn=request.POST.get('orgsenderphn')
        org_password=request.POST.get('orgpassword')
        orglogo=request.FILES['orglogo'].name

        c=Organisations(orgname = org_name,orgemail = org_email,orgcc=org_cc,orgsendermail=org_sender_email,orgsenderphn=org_sender_phn,orgpassword=org_password,orglogo=orglogo)
        c.save()
        handle_uploaded_file1(request.FILES['orglogo'])
        return HttpResponse(request.FILES['orglogo'].name)
        #return render(request,'organisations/orgRegister.html')
       # return HttpResponse(request.FILES['picture'].name)
    else:
        return render(request,'organisations/orgRegister.html')
def orglogin(request):
        if request.method == 'POST':
                
                org_email=request.POST.get('orgemail')
                org_password=request.POST.get('orgpass')
                db = sqlite3.connect('home/ayushruia/Documents/environments/my_env/PersonalWebsite/db.sqlite3')
                c = db.cursor()
                c.execute('SELECT * FROM organisations WHERE orgemail = ? AND orgpassword = ?', (org_email, org_password))
                if c.fetchall():
                    return render(request,'organisations/orgRegister.html')
                else:
                    print('Login failed')
                    return render(request,"organisations/orglogin.html")
                
        else:
                
            return render(request,"organisations/orglogin.html")

def show(request):
    orga= Organisations.objects.all()
    return render(request,"organisations/showreg.html",{'org':orga})

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
   
        
def showcust(request):
    customers = Customer.objects.all()
    return render(request,"organisations/showcust.html",{'customers':customers})




def editcust(request, id):
        customer = Customer.objects.get(id=id)
        if request.method == "POST":
                org_id=request.POST.get('orgid')
                cust_name=request.POST.get('custname')
                cust_email=request.POST.get('custemail')
                cust_phn=request.POST.get('custphone')
                cust_status=request.POST.get('custstatus')
        
                customer = Customer(orgid=org_id, custname=cust_name, custemail=cust_email,custphn=cust_phn,custstatus=cust_status )
                customer.save()

        return render(request,'organisations/editcust.html',{'customer': customer})

def updatecust(request, id):
        customer = Customer.objects.get(id=id)
        form = CustomerForm(request.POST, instance = customer)  
        form.save()  
        return redirect("/showcust") 
        

def destroy(request,id):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return redirect("/showcust/")

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
def email(request):
    subject = 'Thank you for registering to our site'
    message = 'WElcome to trsck Debtors'
    email_form = settings.EMAIL_HOST_USER
    recipient_list = ['dipakmca11132@gmail.com','subhasishk149@gmail.com']
    send_mail(subject,message,email_form,recipient_list)
    return HttpResponse("ok")

scheduler = BackgroundScheduler()
job = None
def start_job():
    global job
    job = scheduler.add_job(email, 'interval', seconds=3600)
    try:
        scheduler.start()
    except:
        pass