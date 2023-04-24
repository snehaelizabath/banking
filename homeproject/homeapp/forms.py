from django import forms

from homeapp.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','DOB','age','phonenumber','email']
