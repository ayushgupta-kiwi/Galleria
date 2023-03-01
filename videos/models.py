from django.db import models

from Galleria.settings import AUTH_USER_MODEL


class VideoGallery(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='videos')

    class Meta:
        db_table = 'VideoGallery'


class Video(models.Model):
    video_gallery = models.ForeignKey(VideoGallery, on_delete=models.CASCADE, related_name='video')
    video = models.FileField(upload_to='media/', null=True)

    class Meta:
        db_table = 'Video'
