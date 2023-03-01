from django.contrib import admin

from images.models import ImageGallery, Image


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    """
        Define which fields to display in the list view of the admin page
    """
    list_display = ('id', 'name')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
        Define which fields to display in the list view of the admin page
    """
    list_display = ('id', 'image')
