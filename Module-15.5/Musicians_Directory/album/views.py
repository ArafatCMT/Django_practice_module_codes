from django.shortcuts import render, redirect
from album.forms import AlbumForm
from album.models import Album
# Create your views here.
def album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('album')
    else:
        form = AlbumForm()
    return render(request, 'album.html' , {'form': form})


def edit_album(request, id):
    data = Album.objects.get(pk = id)
    edit_album = AlbumForm(instance=data)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=data)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('homepage')
    else:
        form = AlbumForm()
    return render(request, 'album.html' , {'form': edit_album})

