from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

from .models import Order
 
class CustomUserForm(UserCreationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
  email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
  class Meta:
    model=User
    fields=['username','email','password1','password2']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'delivery_instructions']
        widgets = {
            'delivery_instructions': forms.Textarea(attrs={
                'placeholder': 'e.g., Leave at the doorstep, don’t ring the bell',
                'rows': 3
            }),
        }