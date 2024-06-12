from django.urls import path
from musician import views
urlpatterns = [
    path('add/', views.AddMusician.as_view() , name='add_musician'),
    path('edit/<int:id>', views.EditMusicianData.as_view() , name='edit_musician'),
    path('delete/<int:id>', views.DeleteMusician.as_view() , name='delete_musician'),
]
