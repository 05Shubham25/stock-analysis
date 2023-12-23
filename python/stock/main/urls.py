
from django.urls import path

from  . import views

urlpatterns = [
    path('',views.stocktracker,name='tracker'),
    path('',views.stockpicker,name='picker')
]
