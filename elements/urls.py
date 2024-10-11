from django.urls import path
from . import views

urlpatterns = [
    path('', views.element_list, name='element_list'),
]
