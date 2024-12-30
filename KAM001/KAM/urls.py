from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('add/', views.add_lead, name='add_lead'),
    path('<email>/edit/', views.edit_lead, name='edit_lead'),
    path('<email>/del/', views.del_lead, name='del_lead'),
    path('register/', views.register, name='register')
]