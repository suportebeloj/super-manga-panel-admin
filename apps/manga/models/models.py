from django.db import models


# Create your models here.


class Chapter(models.Model):
    pass


class Season(models.Model):
    pass


class Author(models.Model):
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=64, blank=True)
    birth = models.DateTimeField(blank=True)
    death = models.DateTimeField(blank=True)
    nationality = models.CharField(blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Manga(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    author = models.ManyToManyField(Author)
    publication_year = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
