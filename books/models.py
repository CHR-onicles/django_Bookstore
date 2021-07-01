from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    authors = models.CharField(max_length=256, default='Unknown')
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title
