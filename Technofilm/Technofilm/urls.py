from django.urls import path
from main import views
  
urlpatterns = [
    path("", views.main),
    path('search', views.search),
    path('film/<int:id>', views.film),
    path("index", views.index),
    path("find",views.find),
]
