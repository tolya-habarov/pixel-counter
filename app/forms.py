from django import forms

from app import models


class UploadImageForm(forms.ModelForm):
    """Upload new image form"""

    class Meta:
        model = models.Image
        fields = '__all__'
        labels = {'file': 'Image file'}


class HexColorForm(forms.Form):
    hex_color = forms.CharField(
        label='Hex color',
        max_length=7,
        min_length=7,
    )