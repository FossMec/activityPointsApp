from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['student','registration_no','class_list','password']



class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['registration_no','password']
