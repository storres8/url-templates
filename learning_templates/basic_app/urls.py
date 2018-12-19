from django.urls import path
from basic_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
