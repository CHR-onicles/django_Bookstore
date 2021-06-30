from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    page_count = models.IntegerField(null=True)
    thumbnail_url = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256)
    long_description = models.TextField(null=True)
