from django.urls import path
from first_app import views

urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact)
]