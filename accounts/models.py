from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


def user_directory_path(instance, filename):
    return f'{instance.image_gallery.user.username}/{instance.image_gallery.name}/{filename}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_directory(sender, instance, created, **kwargs):
    if created:
        media_directory_path = os.path.join(settings.MEDIA_ROOT)
        user_directory_path1 = os.path.join(media_directory_path, instance.username)
        if not os.path.exists(media_directory_path):
            os.makedirs(media_directory_path)
        if not os.path.exists(user_directory_path1):
            os.makedirs(user_directory_path1)


class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=16, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.username


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')
    token = models.CharField(max_length=255)

    class Meta:
        db_table = 'Token'
