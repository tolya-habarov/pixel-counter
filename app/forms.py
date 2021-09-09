from django import forms

from app import models


class UploadImageForm(forms.ModelForm):
    """Upload new image form"""

    class Meta:
        model = models.Image
        fields = '__all__'
        labels = {'file': 'Image file'}