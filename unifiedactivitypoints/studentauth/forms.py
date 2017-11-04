from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','registration_no','class_no','password']



class LoginForm(forms.ModelForm):
    class Meta:
        models = UserProfile
        fields = ['registration_no','password']
