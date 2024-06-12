from django.shortcuts import render
from album import forms
from django.views.generic import CreateView, UpdateView
from album import models
from django.urls import reverse_lazy
# Create your views here.

class AddAlbum(CreateView):
    model = models.Album
    form_class = forms.ALbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('add_album')


class EditAlbumData(UpdateView):
    model = models.Album
    form_class = forms.ALbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
