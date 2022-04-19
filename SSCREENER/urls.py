from tokenize import Name
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('<str:tid>',views.ticker, name='ticker'),
    path('',views.index, name='index'),
]