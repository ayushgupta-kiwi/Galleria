from django.contrib import admin

from accounts.models import User, Token


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
        Define which fields to display in the list view of the admin page
    """
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'contact', 'password')


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    """
        Define which fields to display in the list view of the admin page
    """
    list_display = ('id', 'token')
