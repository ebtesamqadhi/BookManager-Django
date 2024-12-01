from django import forms
from .models import *

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {'name': forms.TextInput(attrs={'class':'form-control'})}

class Bookform(forms.ModelForm):
    class Meta:        # عشان اجيب ال fild اللي داخل المودل
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'rental_price_day',
            'rental_period',
            'total_rental',
            'state',
            'category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day': forms.NumberInput(attrs={'class':'form-control', 'id':'rentprice'}),
            'rental_period': forms.NumberInput(attrs={'class':'form-control', 'id':'rentperiod'}),
            'total_rental' : forms.NumberInput(attrs={'class':'form-control', 'id':'totalrent'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }