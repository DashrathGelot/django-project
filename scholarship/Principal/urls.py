from django.urls import path
from .views import t_regis,t_data
urlpatterns=[
    path('register/',t_regis),
    path('data/',t_data),

]