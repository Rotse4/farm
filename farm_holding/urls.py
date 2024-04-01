from django.urls import path
from . import views

urlpatterns =[
    # path('', views.register),
    path('farm', views.post_farm_holdings),
]