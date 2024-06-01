from django import forms
from first_app.models import HealthForm

class AdmissionForm(forms.Form):
    name = forms.CharField(label='Name', required=False, help_text= 'Write your full name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    date_of_birth = forms.DateField(label='Dath Of Birth', widget=forms.DateInput(attrs={'type': 'date',}), required=False)
    email = forms.EmailField(label='Email Address', required=False, widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Write you address here...', 'row':3}), required=False)
    GENDER = [
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other')
    ]
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, required=False)
    UNIVERSITY = [
        ('KUET', 'Khulna University of Engineering & Technology'),
        ('BUET', 'Bangladesh University of Engineering and Technology'),
        ('DUET', 'Dhaka University of Engineering and Technology'),
        ('RUET', 'Rajshahi University of Engineering and Technology'),
    ]
    university = forms.MultipleChoiceField(choices=UNIVERSITY, widget=forms.CheckboxSelectMultiple(), label='University' , required=False)
    DEPARTMENT = [
        ('EEE', 'Electrical and Electronics Engineering'), 
        ('CSE', ' Computer Science Engineering'), 
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('RE', 'Robotics Engineering'),
        ('EE', 'Environmental Engineering'),
        ('ChE', 'Chemical Engineering')
        ]
    department = forms.ChoiceField(choices=DEPARTMENT, required=False, label="Department :")
    phone_no = forms.CharField(max_length=12, label='Phone Number' , required=False)
    agree = forms.BooleanField(label='Agree' , required=False)


class HealthModelForm(forms.ModelForm):
    class Meta:
        model = HealthForm
        fields = '__all__'

        labels = {
            'details': 'Please provide details',
            'phone_no' : 'Phone Number',
            'symptoms' : 'Are you experiencing any of the following symptoms?',
            'vaccine' : 'Have you received the COVID-19 vaccine?',
            'condition' : 'Do you have any existing medical conditions?',
            'file' : 'Please provide medical report file'

        }
        SYMPTOMS = [('fever', 'Faver'), ('cough', 'Cough'), ('brath','Shortness of Breath'), ('headache', 'Headache')]

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : 'Please enter your name'}),
            'phone_no': forms.TextInput(attrs={'placeholder': '### ### ####'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Please enter your email'}),
            'date_of_birth' : forms.DateInput(attrs={'type': 'date'}),
            'gender' : forms.RadioSelect(),
            'condition': forms.RadioSelect(),
            
            'symptoms' : forms.CheckboxSelectMultiple(choices=SYMPTOMS),
            'vaccine' : forms.RadioSelect(),
            'date' : forms.DateInput(attrs={'type': 'date'})
        }

        help_texts = {
            'file' : 'Please select pdf file'
        }
