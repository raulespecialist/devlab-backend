from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('buy/', views.buy, name='buy'),
    path('catalogue/', views.catalogue, name='catalogue'),
    #path('sell/', views.sell, name='sell'),
]
