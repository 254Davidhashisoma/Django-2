from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



from .models import Order


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(max_length=100, help_text='Required')
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

