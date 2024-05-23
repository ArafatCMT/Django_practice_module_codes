from django.urls import path
from first_app import views

urlpatterns = [
    path('django_template_filters/', views.template_filters)
]