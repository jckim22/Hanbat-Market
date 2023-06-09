from django import forms
from django.forms import widgets
from .models import Board


class RegistForm(forms.ModelForm):
    class Meta:
        
        model = Board
        image = forms.ImageField()

        
        fields = ['title', 'author','publisher','minPrice','maxPrice','kakaoId','imgfile','content','under_line','written','page_named','page_age','ripped']  # '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-contro   l'}),
            'minPrice' : forms.TextInput(attrs={'class': 'form-control'}),
            'maxPrice' : forms.TextInput(attrs={'class': 'form-control'}),
            'kakaoId' : forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'under_line': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'written' : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'page_named': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'page_age': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ripped': forms.CheckboxInput(attrs={'class': 'form-control'}),
            
            
        }
        