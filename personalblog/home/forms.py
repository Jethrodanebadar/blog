from django import forms

from .models import blog_data

class Blogform(forms.ModelForm):
    class Meta:
        model = blog_data
        fields = ('title', 'content', 'author', 'image')
        
    def clean_title(self):
        title= self.cleaned_data['title']
        if not title:
            return "Untitled"
        return title



