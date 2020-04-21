from django.urls import path
from .views import hello,datam
urlpatterns=[
    path('hello/',hello),
    path('data/',datam)
]