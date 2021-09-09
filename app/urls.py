from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views


urlpatterns = [
    path('', views.UploadImageView.as_view(), name='upload'),
    path('images/<int:pk>', views.DetailImageView.as_view(), name='image_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)