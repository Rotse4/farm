from django.urls import path
from . import views

urlpatterns =[
    path('', views.register),
    path('details', views.get_farmers),
    path('geography', views.geography),
    path('compined', views.compined),

]