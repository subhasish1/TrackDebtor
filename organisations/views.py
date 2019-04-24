from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'organisations/index.html')
def portfolio(request):
    return render(request,'organisations/portfolio.html')
def orgreg(request):
	if request.method == 'POST':
		form.save()
		#return redirect ('success')
	else:

		return render(request,'organisations/orgRegister.html')
def custreg(request):
	#if request.method == 'POST':
	#	form.save()
		return render(request,'organisations/customer.html')
	#else:
	#	return redirect('success')		

