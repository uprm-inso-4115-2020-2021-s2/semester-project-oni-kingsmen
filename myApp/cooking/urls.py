from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cooking-home'),
    path('about/', views.about, name='cooking-about'),
    path('addRecipe/', views.addRecipe, name='addRecipe'),
    path('search/', views.search, name='cooking-search')
]


