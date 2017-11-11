from django import forms
from . models import *


class FormActivityPoint(forms.ModelForm):
    class Meta:
        model = ActivityPoint
        fields = ('title', 'description', 'points')

    def __init__(self, *args, **kwargs):
        super(FormActivityPoint, self).__init__(*args, **kwargs)
        """self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'autocorrect': 'off',
                                                  'autocapitalize': 'none',
                                                  'type': 'email'})"""

