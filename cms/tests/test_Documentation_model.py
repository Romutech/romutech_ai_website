from django.test import TestCase
from cms.models import Documentation


class DocumentationTest(TestCase):
    def setUp(self):
        self.model = Documentation

        self.title = "Documentation de l'API"
        self.description = "Une documentation est disponible. Vous y trouverez les différentes routes existantes, etc."
        self.button = "Documentation"

        self.bad_title = "Bad title"
        self.wrong_description = "Wrong description"
        self.bad_button = "Bad button"

    def test_create_documentation(self):
        self.assertEquals(Documentation.objects.count(), 0)

        documentation = self.model.objects.create(title=self.title, description=self.description, button=self.button)

        self.assertEquals(Documentation.objects.count(), 1)
        self.assertEquals(documentation.title, self.title)
        self.assertEquals(documentation.description, self.description)
        self.assertEquals(documentation.button, self.button)
        self.assertNotEquals(documentation.title, self.bad_title)
        self.assertNotEquals(documentation.description, self.wrong_description)
        self.assertNotEquals(documentation.button, self.bad_button)


    def test_read_documentation(self):
        self.model.objects.create(title=self.title, description=self.description, button=self.button)

        self.assertEquals(self.model.objects.count(), 1)

        documentation = self.model.objects.latest('id')

        self.assertEquals(documentation.title, self.title)
        self.assertEquals(documentation.description, self.description)
        self.assertEquals(documentation.button, self.button)
        self.assertNotEquals(documentation.title, self.bad_title)
        self.assertNotEquals(documentation.description, self.wrong_description)
        self.assertNotEquals(documentation.button, self.bad_button)


    def test_update_documentation(self):
        self.model.objects.create(title=self.title, description=self.description, button=self.button)

        self.assertEquals(self.model.objects.count(), 1)

        documentation = self.model.objects.latest('id')

        self.assertEquals(documentation.title, self.title)
        self.assertEquals(documentation.description, self.description)
        self.assertEquals(documentation.button, self.button)

        documentation.title = "New title"
        documentation.save(update_fields=['title'])

        self.assertEquals(documentation.title, "New title")
        self.assertEquals(documentation.description, self.description)
        self.assertEquals(documentation.button, self.button)

    def test_delete_feature(self):
        self.model.objects.create(title=self.title, description=self.description, button=self.button)

        self.assertEquals(self.model.objects.count(), 1)

        documentation = self.model.objects.latest('id')

        documentation.delete()

        self.assertEquals(self.model.objects.count(), 0)
