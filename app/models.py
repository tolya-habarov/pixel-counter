from django.db import models
from django.urls import reverse


class Image(models.Model):
    """Image model"""
    
    file = models.ImageField(upload_to='%Y/%m/%d/')

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})
