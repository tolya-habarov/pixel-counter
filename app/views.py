from django import forms
from django.views.generic import CreateView, DetailView

from app import forms
from app import models


class UploadImageView(CreateView):
    """Upload image view"""

    form_class = forms.UploadImageForm
    template_name = 'upload.html'

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()


class DetailImageView(DetailView):
    """View specific image"""

    model = models.Image
    template_name = 'image.html'
    context_object_name = 'image'
