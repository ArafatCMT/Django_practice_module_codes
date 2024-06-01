from django.db import models
import datetime 

# Create your models here.
class HealthForm(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,)
    date_of_birth = models.DateField()
    GENDER = [
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other')
    ]
    gender = models.CharField(max_length=10, choices=GENDER, default=None)
    email = models.EmailField()
    phone_no = models.CharField(max_length=11)
    CONDITION = [('yes', 'Yes'), ('no', 'No')]
    condition = models.CharField(max_length=5, choices=CONDITION, default=None)
    # SYMPTOMS = [('fever', 'Faver'), ('cough', 'Cough'), ('brath','Shortness of Breath'), ('headache', 'Headache')]
    symptoms = models.CharField(max_length=30,default=None)
    vaccine = models.CharField(max_length=10,choices=CONDITION, default=None)
    details = models.TextField()
    file = models.FileField()
    date = models.DateField(default=datetime.datetime.now())
