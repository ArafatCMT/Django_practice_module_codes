from django.urls import path
from album.views import album, edit_album

urlpatterns = [
    path('add/', album, name = 'album'),
    path('edit_album/<int:id>', edit_album, name = 'edit_album'),
]