from django import forms
from django.core.validators import FileExtensionValidator

from .models import File


class IndexForm(forms.ModelForm):
    word = forms.CharField(help_text='Слово для поиска в файле')
    file = forms.FileField()
    class Meta:
        model = File
        fields = ['file', 'word']
