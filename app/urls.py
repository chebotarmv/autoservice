from django.urls import path
from . import views


urlpatterns = [
    path('', views.master_list, name='master_list'),
]