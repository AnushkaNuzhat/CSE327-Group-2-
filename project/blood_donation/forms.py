from .models import *
from django.forms import ModelForm
from django import forms


class BloodRequestForm(ModelForm):
    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('', 'Select Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    blood_group = forms.CharField(widget=forms.Select(choices=BLOOD_GROUP_CHOICES))
    needed_within = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta: # Provide an association between the ModelForm and a model
        model = BloodRequestModel # And information about the fields in the model
        fields = '__all__' # Or specify the fields to include (i.e. not include the ones we don't want)
        exclude = ['user', 'is_active'] # Or specify the fields to exclude from the form
