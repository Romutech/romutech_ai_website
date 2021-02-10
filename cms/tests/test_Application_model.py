from django.test import TestCase
from cms.models import Application


class ApplicationTest(TestCase):
    def setUp(self):
        self.model = Application

        self.title = "Lancer L'application Romutech AI"
        self.button = "Romutech AI"

        self.bad_title = "Bad title"
        self.wrong_button = "Wrong button"

    def test_create_application(self):
        self.assertEquals(Application.objects.count(), 0)

        application = self.model.objects.create(title=self.title, button=self.button)

        self.assertEquals(Application.objects.count(), 1)
        self.assertEquals(application.title, self.title)
        self.assertEquals(application.button, self.button)
        self.assertNotEquals(application.title, self.bad_title)
        self.assertNotEquals(application.button, self.wrong_button)

    def test_read_application(self):
        self.model.objects.create(title=self.title, button=self.button)

        self.assertEquals(self.model.objects.count(), 1)

        application = self.model.objects.latest('id')

        self.assertEquals(application.title, self.title)
        self.assertEquals(application.button, self.button)
        self.assertNotEquals(application.title, self.bad_title)
        self.assertNotEquals(application.button, self.wrong_button)

    def test_update_application(self):
        self.model.objects.create(title=self.title, button=self.button)

        self.assertEquals(self.model.objects.count(), 1)

        application = self.model.objects.latest('id')

        self.assertEquals(application.title, self.title)
        self.assertEquals(application.button, self.button)

        application.title = "New title"
        application.save(update_fields=['title'])

        self.assertEquals(application.title, "New title")
        self.assertEquals(application.button, self.button)

    def test_delete_application(self):
        self.model.objects.create(title=self.title, button=self.button)

        self.assertEquals(self.model.objects.count(), 1)

        application = self.model.objects.latest('id')

        application.delete()

        self.assertEquals(self.model.objects.count(), 0)
