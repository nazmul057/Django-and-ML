from django import forms

from .models import TestImage

class TestImageForm(forms.ModelForm):
    class Meta:
        model = TestImage
        fields = ('picture',)