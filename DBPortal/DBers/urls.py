from django.urls import path
from .views import index, addDBers

urlpatterns = [
    path('', index, name='index'),
    path('Staff/addDBers/', addDBers, name='addDBers'),
]
