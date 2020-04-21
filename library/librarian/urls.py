from django.urls import path
from .views import b_data

urlpatterns=[
    path('',b_data)
]