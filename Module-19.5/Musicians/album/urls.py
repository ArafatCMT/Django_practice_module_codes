from django.urls import path
from album import views
urlpatterns = [
    path('add/', views.AddAlbum.as_view(), name='add_album'),
    path('edit/<int:id>', views.EditAlbumData.as_view(), name='edit_album'),
]