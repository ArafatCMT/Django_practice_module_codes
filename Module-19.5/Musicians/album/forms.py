from album.models import Album
from django import forms

class ALbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'