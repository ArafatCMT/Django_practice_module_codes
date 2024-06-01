from django.shortcuts import render, redirect
# from musician.forms import MusicianForm
from . import models,forms
# Create your views here.
def musician_form(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('musician')
    else:
        form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': form})

def delete_musician(request, id):
    models.Musician.objects.get(pk = id).delete()
    return redirect('homepage')

def edit_musician(request, id):
    musician = models.Musician.objects.get(pk = id)
    _edit_musician = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': _edit_musician})



