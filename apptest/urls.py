from django.urls import path
from apptest import views

urlpatterns = [
    path('sign_srv/', views.sign_srv)
]