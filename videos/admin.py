from django.contrib import admin

from videos.models import VideoGallery, Video


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    """
        Define which fields to display in the list view of the admin page
    """
    list_display = ('id', 'name')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """
        Define which fields to display in the list view of the admin page
    """
    list_display = ('id', 'video')
