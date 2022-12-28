from django.urls import path
from .views import  home_page, export_csv

urlpatterns =[
    path('', home_page, name="home_page"),
    path('export_buy/', export_csv, name="export_csv")
]
