from django.shortcuts import render, redirect
from django.conf.urls.static import static
from .models import Organisations , Customer,Outstanding,Product
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from organisations.forms import CustomerForm
from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models import Count, Q
from django.db import connection
from django.contrib import messages
#from django.template.loader import render_to_string

#>>>>>>> 0e74b8e2590a34a80fb82175d5afa6408be8ec28



def index(request):
    return render(request,'organisations/index.html')
def portfolio(request):
    return render(request,'organisations/portfolio.html')

def handle_uploaded_file1(f):  
    with open('organisations/static/organisations/media/'+f.name, 'wb+') as destination:  
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


        subject = 'Welcome To TRACK DEBTORS'
        message = ('Dear ' + org_name + 
            ' Your Registration is successfully'+
            'username: '+org_email +
            'password: '+org_password)

        email_form = settings.EMAIL_HOST_USER
        recipient_list = [org_email]
        send_mail(subject,message,email_form,recipient_list)



        return HttpResponse(request.FILES['orglogo'].name)
        #return render(request,'organisations/orgRegister.html')
        #return HttpResponse(request.FILES['picture'].name)
    else:
        return render(request,'organisations/orgRegister.html')
def orglogin(request):
        if request.method == 'POST':
                
                org_email=request.POST.get('orgemail')
                org_password=request.POST.get('orgpass')
                k=Organisations.objects.filter(orgemail=org_email, orgpassword=org_password)
                #request.session['orgmail'] = "jain"
                #print(orgmail)
                if k.exists():
                    #sweetify.success(self.request, 'You successfully logged in!')
                    #request.session['username'] = org_email
                    orgdata = Organisations.objects.get(orgemail=org_email)
                    request.session['orgid'] = orgdata.id
                    request.session['logged_in'] = True
                    return render(request,'organisations/dashboard_main_content.html',{'orgdata' : orgdata })
                else:
                    messages.error(request,"Invalid Username and password try again!!")
                    return render(request,"organisations/orglogin.html")   
        else:   
            return render(request,"organisations/orglogin.html")

def show(request):
    orga= Organisations.objects.all()
    return render(request,"organisations/showreg.html",{'org':orga})

def custreg(request):
    if request.session.has_key('orgid'):
        org_id=request.session['orgid']
       # print(org_id)
        orgdata = Organisations.objects.get(id=org_id)

        #print(orgdata.orgname)
        if request.method == 'POST':
                
                
            #print(org_id)
            cust_name=request.POST.get('custname')
            cust_email=request.POST.get('custemail')
            cust_phn=request.POST.get('custphone')
            cust_status=request.POST.get('custstatus')
            
            cust = Customer(orgid=org_id, custname=cust_name, custemail=cust_email,custphn=cust_phn,custstatus=cust_status )
            cust.save()
            messages.success(request, 'Profile details updated.')
            return render(request, 'organisations/customer.html',{'orgdata' : orgdata})
        else:
            return render(request, 'organisations/customer.html',{'orgdata':orgdata})
    else:
        messages.error(request, 'You Are Not Logged In!!!')
        return render(request, 'organisations/orglogin.html')
   
        
def showcust(request):
    if request.session.has_key('orgid'):
            
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        customers = Customer.objects.filter(orgid=org_id)
        return render(request,"organisations/showcust.html",{'customers':customers,'orgdata' :orgdata})




def editcust(request, id):
    if request.session.has_key('orgid'):
        customer = Customer.objects.get(id=id)
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        
        if request.method == "POST":
                org_id=request.POST.get('orgid')
                cust_name=request.POST.get('custname')
                cust_email=request.POST.get('custemail')
                cust_phn=request.POST.get('custphone')
                cust_status=request.POST.get('custstatus')
                customer = Customer(orgid=org_id, custname=cust_name, custemail=cust_email,custphn=cust_phn,custstatus=cust_status )
                customer.save()
                return render(request,'organisations/showcust.html.html',{'customer': customer,'orgdata' :orgdata})
        else:
            return render(request,'organisations/editcust.html',{'customer': customer,'orgdata' :orgdata})
    else:
        messages.error(request, 'You Are Not Logged In!!!')
        return render(request, 'organisations/orglogin.html')

def updatecust(request, id):
    if request.session.has_key('orgid'):
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        
        customer = Customer.objects.get(id=id)
        if request.method == 'POST':
                
                
            #print(org_id)
            cust_name=request.POST.get('custname')
            cust_email=request.POST.get('custemail')
            cust_phn=request.POST.get('custphn')
            cust_status=request.POST.get('custstatus')
            Customer.objects.filter(id=id).update(custname=cust_name, custemail=cust_email,custphn=cust_phn,custstatus=cust_status)

            #cust = Customer(orgid=org_id, custname=cust_name, custemail=cust_email,custphn=cust_phn,custstatus=cust_status )
            #cust.update()
            messages.success(request, 'Profile details updated.')
            return redirect("/showcust/")
        else:
            return render(request, 'organisations/customer.html',{'orgdata':orgdata})

        #form = CustomerForm(request.POST, instance = customer) 
       # if form.is_valid(): 
            #form.save()
            #return redirect("/showcust/")
    else:
        return render(request,'organisations/showcust.html',{'customer': customer,'orgdata' :orgdata})

def destroy(request,id):
    if request.session.has_key('orgid'):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return redirect("/showcust/")
    else:
        return render(request,'organisations/editcust.html',{'customer': customer})
def outstanding(request):
    if request.session.has_key('orgid'):
        
        org_id=request.session['orgid']
        customer = Customer.objects.filter(orgid=org_id)
        orgdata = Organisations.objects.get(id=org_id)

        if request.method == 'POST':
        
            
            cust_id=request.POST.get('custid')
            print(cust_id)
            bill_no=request.POST.get('bill_no')
            bill_amt=request.POST.get('bill_amt')
            due_amt=request.POST.get('due_amt')
            bill_date=request.POST.get('bill_date')
            cleared_on=request.POST.get('cleared_on')
            credit_period = request.POST.get('creditperiod')

            p = Outstanding(orgid=org_id, custid=cust_id, bill_no=bill_no, bill_amt=bill_amt, due_amt=due_amt, bill_date=bill_date, cleared_on=cleared_on,creditperiod=credit_period )
            p.save()
            messages.success(request, 'Outstanding details updated.')
            return render(request,'organisations/outstanding.html',{'customer': customer,'orgdata' :orgdata})
        else:
            return render(request,'organisations/outstanding.html',{'customer': customer,'orgdata' :orgdata})
    else:
        messages.error(request, 'You Are Not Logged In!!!')
        return render(request, 'organisations/orglogin.html')

def email(request,id):
    cust = Customer.objects.get(id=id)
    cust_email = cust.custemail
    print(cust_email)


    #list=Outstanding.objects.filter(due_amt > 0)
    #elist=[]
    #for p in Customer.objects.raw("select c.custemail from customer c,outstanding o where c.id=o.custid and o.due_amt > 0 "):
        #elist.append(p)
    #c = connection.cursor()
    #c.execute('SELECT * FROM customer')
    #c.execute("select c.custemail from customer c,outstanding o where c.id=o.custid and due_amt > 0")
    #x=c.fetchall()
    #for k in x:
      #  elist.append(k)
    subject = 'Thank you for registering to our site'
    message = 'WElcome to track Debtors'
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [cust_email]
    send_mail(subject,message,email_form,recipient_list)
    return HttpResponse(okk)

    scheduler = BackgroundScheduler()
    job = None
    def start_job():
        global job
        job = scheduler.add_job(email, 'interval', seconds=60)
        try:
            scheduler.start() 
        except:
            pass
def showdebtors(request):
    if request.session.has_key('orgid'):
        
        #customer = Customer.objects.get(id=id)
            org_id=request.session['orgid']
            orgdata = Organisations.objects.get(id=org_id)
            data2 = Customer.objects.raw('select c.id as id ,c.id,c.custname,o.bill_no,o.bill_amt,o.due_amt,o.bill_date,o.cleared_on,o.creditperiod from customer c, outstanding o where c.id=o.custid and o.orgid=1')
            
            return render(request,"organisations/showdebt.html",{'debtors': data2,'orgdata' :orgdata})
        
    else:
         messages.error(request, 'You Are Not Logged In!!!')
         return render(request, 'organisations/orglogin.html')

    
def newchart(request):
    if request.session.has_key('orgid'):
        
        
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        dataset = Outstanding.objects.raw('select o.id as id, o.id, o.bill_date,o.bill_amt,o.due_amt from outstanding o')
        return render(request, 'organisations/newchart.html', {'dataset': dataset,'orgdata' :orgdata})
    else:
        messages.error(request, 'You Are Not Logged In!!!')
        return render(request, 'organisations/orglogin.html')
    
def orglogout(request):
    try:
        del request.session['orgid']
        messages.success(request, 'You are sucessfully logout!!Please log!!!')
        return render(request, 'organisations/orglogin.html')
    except KeyError:
        return render(request, 'organisations/orglogin.html')


def resetpassword(request):
    if request.session.has_key('orgid'):
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        if request.method == 'POST':
            

            old_pass = request.POST.get('oldpassword')
            new_pass = request.POST.get('newpassword')
            print(orgdata.orgpassword)

            if orgdata.orgpassword == old_pass:
                Organisations.objects.filter(id=org_id).update(orgpassword=new_pass)
                messages.success(request, 'Password changed!! Please login!')
                return render(request, 'organisations/orglogin.html')
            else:
                messages.error(request, 'please enter correct old password')
                return render(request, 'organisations/orglogin.html')
        else:
            return render(request, 'organisations/orgresetpassword.html')
    else:
        messages.error(request, 'You Are Not Logged In!!!')
        return render(request, 'organisations/orglogin.html')

def productregister(request):
    if request.session.has_key('orgid'):
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        if request.method == 'POST':
            prdt_brand=request.POST.get('brand')
            prdt_quantity=request.POST.get('quantity')
            prdt_price=request.POST.get('price')
            prdt_gst=request.POST.get('gst')
            
            prdt = Product(orgid=org_id, brand=prdt_brand, quantity=prdt_quantity,price=prdt_price,gst=prdt_gst )
            prdt.save()
            messages.success(request, 'Product is created')
            return render(request, 'organisations/productRegister.html',{'orgdata':orgdata })
        else:
            return render(request, 'organisations/productRegister.html',{'orgdata':orgdata })
    else:
        messages.error(request, 'You Are Not Logged In!!!')
        return render(request, 'organisations/orglogin.html')


def showproduct(request):
    if request.session.has_key('orgid'):
            
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        products = Product.objects.filter(orgid=org_id)
        return render(request,"organisations/showproduct.html",{'products':products,'orgdata' :orgdata})



def editproduct(request, id):
    if request.session.has_key('orgid'):
        product = Product.objects.get(id=id)
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        
        if request.method == "POST":
                org_id=request.POST.get('orgid')
                prdt_brand=request.POST.get('brand')
                prdt_quantity=request.POST.get('quantity')
                prdt_price=request.POST.get('price')
                prdt_gst=request.POST.get('gst')
                product = Product(orgid=org_id, brand=prdt_brand, quantity=prdt_quantity,price=prdt_price,gst=prdt_gst )
                product.save()
                return render(request,'organisations/showproduct.html.html',{'product': product,'orgdata' :orgdata})
        else:
            return render(request,'organisations/editproduct.html',{'product': product,'orgdata' :orgdata})
    else:
        messages.error(request, 'You Are Not Logged In!!!')
        return render(request, 'organisations/orglogin.html')


def updateproduct(request, id):
    if request.session.has_key('orgid'):
        org_id=request.session['orgid']
        orgdata = Organisations.objects.get(id=org_id)
        
        product = Product.objects.get(id=id)
        if request.method == 'POST':
                
                
            prdt_brand=request.POST.get('brand')
            prdt_quantity=request.POST.get('quantity')
            prdt_price=request.POST.get('price')
            prdt_gst=request.POST.get('gst')
            Product.objects.filter(id=id).update(brand=prdt_brand, quantity=prdt_quantity,price=prdt_price,gst=prdt_gst)


            messages.success(request, 'Product details updated.')
            return redirect("/showproduct/")
        else:
            return render(request, 'organisations/productRegister.html',{'orgdata':orgdata})


def destroyproduct(request,id):
    if request.session.has_key('orgid'):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect("/showproduct/")
    else:
        return render(request,'organisations/editproduct.html',{'product': product})