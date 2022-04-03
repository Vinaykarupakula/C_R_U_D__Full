from django.urls import path
from app1 import views

urlpatterns = [
    path('get/', views.display),
    path('edit/<int:pk>', views.edit),
]