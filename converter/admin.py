from django.contrib import admin
from .models import ImageData


@admin.register(ImageData)
class ImageDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('base64_data', 'created_at')
