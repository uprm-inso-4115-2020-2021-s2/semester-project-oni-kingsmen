from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cooking-home'),
    path('about/', views.about, name='cooking-about'),
]


