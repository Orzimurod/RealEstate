from django import forms
from .models import postadvert

class PostadvertForm(forms.ModelForm):
    class Meta:
        model = postadvert
        fields = ['title', 'price', 'category', 'city', 'description', 'image']

