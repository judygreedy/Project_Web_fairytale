from django.urls import path
from ProjectFinal import views

urlpatterns =[
    path('', views.func_Make, name ='make'),
    path('fairytale', views.func_Fairytale, name ='fairytale'),
]