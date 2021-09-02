from django.urls import path
from . import views

urlpatterns = [
    path('procesar/', views.procesar, name='procesar'),
    path('list/', views.list_companies, name='list companies'),
]
