from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(timezone.now())


class Author(models.Model):
    name = models.CharField(max_length=225)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    objects = models.manager

    def __str__(self):
        return self.name
