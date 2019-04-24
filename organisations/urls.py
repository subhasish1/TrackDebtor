from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('orgregister/' ,views.orgreg, name='orgreg'),
    path('portfolio/' ,views.portfolio, name='portfolio'),
	path('custregister/' ,views.custreg, name='custreg'),
	  
]
