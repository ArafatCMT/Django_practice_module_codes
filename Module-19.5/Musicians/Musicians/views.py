from django.shortcuts import render
from album.models import Album

def home(request):
    album_list = Album.objects.all()
    return render(request, 'home.html', {'list': album_list})