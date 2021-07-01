from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    page_count = models.IntegerField(default=0)
    thumbnail_url = models.CharField(max_length=256, null=True)
    short_description = models.CharField(max_length=256, null=True)
    long_description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title
