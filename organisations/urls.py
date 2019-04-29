from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('orgregister/' ,views.orgreg, name='orgreg'),
    path('portfolio/' ,views.portfolio, name='portfolio'),
	path('custregister/' ,views.custreg, name='custreg'),
	path('outstanding/',views.outstanding, name='outstanding'),
    path('mail/',views.email, name='mail'),
    path('display/',views.show, name='show'),
   # path('login/',views.login, name='login'),
]
