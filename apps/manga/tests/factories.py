from datetime import datetime

import factory

from apps.manga.models.models import Manga, Author


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
        django_get_or_create = ('name', 'surname')
    name = ""
    surname = ""
    nationality = ""


class MangaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Manga
        django_get_or_create = ('title',)

    title = ""
    about = factory.Faker("text")
    created_at = factory.LazyFunction(datetime.utcnow)
    updated_at = factory.LazyFunction(datetime.utcnow)
