from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('orgregister/' ,views.orgreg, name='orgreg'),
    path('portfolio/' ,views.portfolio, name='portfolio'),
	path('custregister/' ,views.custreg, name='custreg'),
	path('outstanding/',views.outstanding, name='outstanding'),
    path('debtors/',views.showdebtors, name='showdebtors'),
    path('mail/<int:id>',views.email, name='email'),
    path('display/',views.show, name='show'),
    path('orglogin/',views.orglogin, name='orglogin'),
    path('showcust/',views.showcust, name='showcust'),
    path('editcust/<int:id>',views.editcust, name='editcust'),
    path('updatecust/<int:id>',views.updatecust, name='updatecust'),
    path('deletecust/<int:id>',views.destroy, name='destroy'),
    path('newchart/',views.newchart,name='newchart'),
    path('orglogout/',views.orglogout,name='orglogout'),
    path('resetpassword/',views.resetpassword,name='resetpassword'),
    path('productregister/',views.productregister,name='productregister'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

