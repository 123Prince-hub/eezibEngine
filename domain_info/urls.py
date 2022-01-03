from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ports/<int:uid>/<str:subd>', views.open_ports, name='ports'),
    path('subdo', views.multi_open_ports, name='multi_ports'),
]