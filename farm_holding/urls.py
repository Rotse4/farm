from django.urls import path
from . import views

urlpatterns =[
    # path('', views.register),
    path('information', views.post_farm_holdings),
]