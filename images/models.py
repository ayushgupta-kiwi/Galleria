from django.db import models
from Galleria.settings import AUTH_USER_MODEL
from accounts.models import user_directory_path


class ImageGallery(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'ImageGallery'


class Image(models.Model):
    image_gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=user_directory_path, null=True)

    class Meta:
        db_table = 'Image'
