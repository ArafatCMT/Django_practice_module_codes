from django.urls import path
from musician.views import musician_form, delete_musician, edit_musician
urlpatterns = [
    path('add/', musician_form, name = 'musician'),
    path('delete_musician/<int:id>', delete_musician, name= 'delete_musicain'),
    path('edit_musician/<int:id>', edit_musician, name = 'edit_musician'),
]