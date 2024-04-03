from django.urls import path
from . import views

urlpatterns =[
    # path('', views.register),
    path('farm', views.post_farm_holdings),
    path('crop', views.crop),
    path('get_crop', views.get_crop),
    path('get_farm', views.get_farm_holdings),
]