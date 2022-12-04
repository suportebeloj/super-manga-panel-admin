from datetime import datetime

import factory

from apps.manga.models.models import Manga


class MangaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Manga
        django_get_or_create = ('title',)

    title = ""
    about = factory.Faker("text")
    created_at = factory.LazyFunction(datetime.utcnow)
    updated_at = factory.LazyFunction(datetime.utcnow)
