from django.db import models


class ImageData(models.Model):
    """Model to store image conversion data"""
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    base64_data = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Image Data"

    class Meta:
        ordering = ['-created_at']
