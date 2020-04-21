from django.urls import path
from .views import S_Register,S_apply

urlpatterns=[
    path('register/',S_Register),
    path('apply/',S_apply)
]