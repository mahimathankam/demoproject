from django import forms
from movie.models import Movie
class Movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"