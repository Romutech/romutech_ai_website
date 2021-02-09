from django.test import TestCase
from .models import Presentation, Application, Api, Documentation, Footer


# **************************************************************************** #
#                            Presentation Tests                                #
# **************************************************************************** #

class PresentationTest(TestCase):
    def setUp(self):
        self.model = Presentation

        self.title = "Romutech AI"
        self.description = "Romutech AI est une solution basée sur l'intelligence artificielle."
        self.features = [
            {
                "title": "Détection de visage",
                "content": "La solution permet de detecter des visages."
            },
            {
                "title": "Floutage des visages.",
                "content": "La solution permet d'automatiser le floutage des visages sur une photo."
            },
            {
                "title": "Comptage des personnes",
                "content": "La solution permet le comptage des personnes présentes sur une photo."
            },
            {
                "title": "Détection du port du masque",
                "content": "La solution permet de vérifier le port du masque par les personnes présentes sur la photo."
            }
        ]

        self.bad_title = "Bad title"
        self.wrong_description = "Wrong description"
        self.bad_json_features = [{'title': "Bad title JSON", 'content': "Bad content JSON"}]

    def test_create_presentation(self):
        self.assertEquals(Presentation.objects.count(), 0)

        presentation = self.model.objects.create(title=self.title, description=self.description, features=self.features)

        self.assertEquals(Presentation.objects.count(), 1)
        self.assertEquals(presentation.title, self.title)
        self.assertEquals(presentation.description, self.description)
        self.assertEquals(presentation.features, self.features)
        self.assertNotEquals(presentation.title, self.bad_title)
        self.assertNotEquals(presentation.description, self.wrong_description)
        self.assertNotEquals(presentation.features, self.bad_json_features)

    def test_read_presentation(self):
        self.model.objects.create(title=self.title, description=self.description, features=self.features)

        self.assertEquals(self.model.objects.count(), 1)

        presentation = self.model.objects.latest('id')

        self.assertEquals(presentation.title, self.title)
        self.assertEquals(presentation.description, self.description)
        self.assertEquals(presentation.features, self.features)
        self.assertNotEquals(presentation.title, self.bad_title)
        self.assertNotEquals(presentation.description, self.wrong_description)
        self.assertNotEquals(presentation.features, self.bad_json_features)

    def test_update_presentation(self):
        self.model.objects.create(title=self.title, description=self.description, features=self.features)

        self.assertEquals(self.model.objects.count(), 1)

        presentation = self.model.objects.latest('id')

        self.assertEquals(presentation.title, self.title)
        self.assertEquals(presentation.description, self.description)
        self.assertEquals(presentation.features, self.features)

        presentation.title = "New title"
        presentation.save(update_fields=['title'])

        self.assertEquals(presentation.title, "New title")
        self.assertEquals(presentation.description, self.description)
        self.assertEquals(presentation.features, self.features)

    def test_delete_presentation(self):
        self.model.objects.create(title=self.title, description=self.description, features=self.features)

        self.assertEquals(self.model.objects.count(), 1)

        presentation = self.model.objects.latest('id')

        presentation.delete()

        self.assertEquals(self.model.objects.count(), 0)


# **************************************************************************** #
#                             Application Tests                                #
# **************************************************************************** #

class ApplicationTest(TestCase):
    def setUp(self):
        self.model = Application

        self.title = "Lancer L'application Romutech AI"
        self.button = "Romutech AI"

        self.bad_title = "Romutech AI"
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


# **************************************************************************** #
#                                 Api Tests                                    #
# **************************************************************************** #

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
