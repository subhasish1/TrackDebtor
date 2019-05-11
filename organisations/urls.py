from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('orgregister/' ,views.orgreg, name='orgreg'),
    path('portfolio/' ,views.portfolio, name='portfolio'),
	path('custregister/' ,views.custreg, name='custreg'),
	path('outstanding/',views.outstanding, name='outstanding'),
    path('debtors/',views.showdebtors, name='showdebtors'),
    path('mail/',views.email, name='mail'),
    path('display/',views.show, name='show'),
    path('orglogin/',views.orglogin, name='orglogin'),
    path('showcust/',views.showcust, name='showcust'),
    path('editcust/<int:id>',views.editcust, name='editcust'),
    path('updatecust/<int:id>',views.updatecust, name='updatecust'),
    path('deletecust/<int:id>',views.destroy, name='destroy'),
    path('start_job',views.start_job, name='start_job'),
]
