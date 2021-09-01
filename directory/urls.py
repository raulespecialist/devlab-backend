from django.urls import path
from . import views

urlpatterns = [
    path('procesar/', views.procesar, name='procesar'),
]
