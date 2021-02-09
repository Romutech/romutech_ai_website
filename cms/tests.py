from django.test import TestCase
from .models import Presentation, Application, Api, Documentation, Footer


#*******************************************************************************
#                             Presentation Tests                               #
#*******************************************************************************

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

