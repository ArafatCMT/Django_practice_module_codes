from django import forms
from musician.models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '### #### ####'}),
            'instrument_type': forms.TextInput(attrs={'placeholder': 'Write instrument type'})
        }