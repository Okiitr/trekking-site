from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm  # this is all for making a  user
from django.contrib.auth.models import User  # this is all for making a  user
from.models import Contact


class ContactForm(forms.ModelForm):
            
            class Meta:
              model = Contact
              fields = ('name','email','subject','msg')



class CreateUser(UserCreationForm):  # this is all for making a  user
      class Meta:
              model = User
              fields = ['first_name','last_name','username','email','password1','password2']