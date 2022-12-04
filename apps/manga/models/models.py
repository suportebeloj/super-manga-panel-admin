from django.db import models


# Create your models here.


class Chapter(models.Model):
    pass


class Season(models.Model):
    pass


class Author(models.Model):
    pass


class Manga(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
