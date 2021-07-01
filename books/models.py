from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    authors = models.CharField(max_length=256, default='Unknown')
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    book_id = models.IntegerField(default=1)

    def __str__(self) -> str:
        if len(self.body) > 20:
            return self.body[:20] + '...'
        else:
            return self.body
