from django.urls import path
from first_app.views import admission_form, health_form

urlpatterns = [
    path('admission_form/', admission_form, name = 'addmission_form'),
    path('health_form/', health_form, name = 'health_form'),
]