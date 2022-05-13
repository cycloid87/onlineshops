from django import forms
from .models import Product

class ProductForm(forms.ModelForm) :
    class Meta :
        model = Product
        fields = ('category', 'name', 'slug', 'image', 'description', 'meta_description', 'price', 'stock', 'available_display', )

