from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['student','registration_no','class_list','password']
        widgets = { 'password': forms.PasswordInput(attrs={'placeholder':'Password'}),

        }



class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['registration_no','password']
        widgets = { 'password': forms.PasswordInput(attrs={'placeholder':'Password'}),
                    'registration_no' : forms.TextInput(attrs={'placeholder':'Registration No'})
        }

