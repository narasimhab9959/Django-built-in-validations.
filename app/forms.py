from django import forms
from django.core import validators


def validate_of_a(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('name error')

def validate_of_len(name):
    if len(name)<=5:
        raise forms.ValidationError('length is high')


class student_form(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_of_a,validate_of_len])
    sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    url=forms.URLField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])