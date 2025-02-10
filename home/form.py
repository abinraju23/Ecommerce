from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Category

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password1',
            'password2': 'Password2',
        }

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)

    class Meta:
        model = Product
        fields = ['category','product_id', 'product_name', 'product_description', 'product_price','product_image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name']
