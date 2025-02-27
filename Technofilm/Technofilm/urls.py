from django.urls import path
from main import views

#все используемые пути
urlpatterns = [
    path("", views.main),
    path('search', views.search),
    path('film/<int:id>', views.film),
    path("find",views.find),
]
