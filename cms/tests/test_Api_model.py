from django.test import TestCase
from cms.models import Api


class ApiTest(TestCase):
    def setUp(self):
        self.model = Api

        self.title = "L'API"
        self.description = "Une API est mise à disponibilité des développeurs."

        self.bad_title = "Bad title"
        self.wrong_description = "Wrong description"

    def test_create_api(self):
        self.assertEquals(Api.objects.count(), 0)

        api = self.model.objects.create(title=self.title, description=self.description)

        self.assertEquals(Api.objects.count(), 1)
        self.assertEquals(api.title, self.title)
        self.assertEquals(api.description, self.description)
        self.assertNotEquals(api.title, self.bad_title)
        self.assertNotEquals(api.description, self.wrong_description)

    def test_read_api(self):
        self.model.objects.create(title=self.title, description=self.description)

        self.assertEquals(self.model.objects.count(), 1)

        api = self.model.objects.latest('id')

        self.assertEquals(api.title, self.title)
        self.assertEquals(api.description, self.description)
        self.assertNotEquals(api.title, self.bad_title)
        self.assertNotEquals(api.description, self.wrong_description)

    def test_update_api(self):
        self.model.objects.create(title=self.title, description=self.description)

        self.assertEquals(self.model.objects.count(), 1)

        api = self.model.objects.latest('id')

        self.assertEquals(api.title, self.title)
        self.assertEquals(api.description, self.description)

        api.title = "New title"
        api.save(update_fields=['title'])

        self.assertEquals(api.title, "New title")
        self.assertEquals(api.description, self.description)

    def test_delete_api(self):
        self.model.objects.create(title=self.title, description=self.description)

        self.assertEquals(self.model.objects.count(), 1)

        api = self.model.objects.latest('id')

        api.delete()

        self.assertEquals(self.model.objects.count(), 0)
