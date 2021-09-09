from typing import Any, Dict

from django import forms
from django.views.generic import CreateView, DetailView

from app import forms
from app import models
from app import services


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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        wt_count, bl_count = services.get_pixel_count(self.object.file.path)
        context['white_count'] = wt_count
        context['black_count'] = bl_count

        return context
