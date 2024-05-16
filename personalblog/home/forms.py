from django import forms
from django.core.exceptions import ValidationError
from .models import blog_data

class Blogform(forms.ModelForm):
    class Meta:
        model = blog_data
        fields = ('title', 'content', 'author')
        
    def clean_author(self):
        author= self.cleaned_data['author']
        if 'Jethro' not in author:
            raise ValidationError("We only accept notes written by Jethro")
        return author