from django import forms
from . models import *


class FormActivityPoint(forms.ModelForm):
    class Meta:
        model = ActivityPoint
        exclude = ('student_id', 'timestamp', 'approved')
        """widgets = {'title': forms.TextInput(attrs={'placeholder': 'Title'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'national_initiatives': forms.BooleanField(label="National Initiatives")}

        """
    def __init__(self, *args, **kwargs):
        super(FormActivityPoint, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Description'})

