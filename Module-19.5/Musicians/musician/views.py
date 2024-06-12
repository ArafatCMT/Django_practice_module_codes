from django.shortcuts import render
from musician import forms
from django.views.generic import CreateView, UpdateView, DeleteView
from musician.models import Musician
from django.urls import reverse_lazy

class AddMusician(CreateView):
    model = Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

class EditMusicianData(UpdateView):
    model = Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

class DeleteMusician(DeleteView):
    model = Musician
    pk_url_kwarg = 'id'
    template_name = 'delete_musician.html'
    success_url = reverse_lazy('homepage')