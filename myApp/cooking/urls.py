from django.urls import path
from . import views
from register import views as v

urlpatterns = [
    path('', views.home, name='cooking-home'),
    path('about/', views.about, name='cooking-about'),
    path('register/', v.register, name="register"),
]


