from datetime import datetime, timedelta

import factory
from faker import Faker
from django.test import TestCase
from .factories import MangaFactory, AuthorFactory


# Create your tests here.
class MangaTestCase(TestCase):

    def setUp(self) -> None:
        faker = Faker()

        self.now = datetime.now()
        self.about = faker.text()
        self.obj = MangaFactory.build(
            title='test manga',
            about=self.about,
            publication_year=self.now + timedelta(hours=5),
            created_at=self.now,
            updated_at=self.now)

    def test_validate_object_data_and_not_have_error(self):
        self.assertEqual(self.obj.title, "test manga")
        self.assertEqual(self.obj.created_at, self.now)
        self.assertEqual(self.obj.updated_at, self.now)
        self.assertIsNotNone(self.obj.about)
        self.assertEqual(self.obj.about, self.about)
        self.assertEqual(self.obj.publication_year, self.now + timedelta(hours=5))


class AuthorTestCase(TestCase):

    def setUp(self) -> None:
        self.obj = AuthorFactory.build(name="test", surname="t", nationality="tst")

    def test_validate_object_data_and_not_have_error(self):
        self.assertEqual(self.obj.name, "test")
        self.assertEqual(self.obj.surname, "t")
        self.assertEqual(self.obj.nationality, "tst")
