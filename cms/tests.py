from django.test import TestCase
from .models import Presentation, Application, Api, Documentation, Footer
from django.conf import settings
from django.urls import reverse

# **************************************************************************** #
#                       Presentation model test                                #
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
#                          Application model test                              #
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
#                             Api model test                                   #
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


# **************************************************************************** #
#                         Documentation model test                             #
# **************************************************************************** #

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

        self.assertEquals(documentation.objects.count(), 1)
        self.assertEquals(documentation.title, self.title)
        self.assertEquals(documentation.description, self.description)
        self.assertEquals(documentation.button, self.button)
        self.assertNotEquals(documentation.title, self.bad_title)
        self.assertNotEquals(documentation.description, self.wrong_description)
        self.assertNotEquals(documentation.button, self.bad_button)


    def test_create_documentation(self):
        self.model.objects.create(title=self.title, description=self.description, button=self.button)

        self.assertEquals(self.model.objects.count(), 1)

        documentation = self.model.objects.latest('id')

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


# **************************************************************************** #
#                            Footer model test                                 #
# **************************************************************************** #

class FooterTest(TestCase):
    def setUp(self):
        self.model = Footer

        self.content = "© Romutech | 2021"

        self.bad_content = "Bad content"

    def test_create_footer(self):
        self.assertEquals(Footer.objects.count(), 0)

        footer = self.model.objects.create(content=self.content)

        self.assertEquals(Footer.objects.count(), 1)
        self.assertEquals(footer.content, self.content)
        self.assertNotEquals(footer.content, self.bad_content)

    def test_read_footer(self):
        self.model.objects.create(content=self.content)

        self.assertEquals(self.model.objects.count(), 1)

        footer = self.model.objects.latest('id')

        self.assertEquals(footer.content, self.content)
        self.assertNotEquals(footer.content, self.bad_content)

    def test_update_footer(self):
        self.model.objects.create(content=self.content)

        self.assertEquals(self.model.objects.count(), 1)

        footer = self.model.objects.latest('id')

        self.assertEquals(footer.content, self.content)

        footer.content = "New content"
        footer.save(update_fields=['content'])

        self.assertEquals(footer.content, "New content")

    def test_delete_footer(self):
        self.model.objects.create(content=self.content)

        self.assertEquals(self.model.objects.count(), 1)

        footer = self.model.objects.latest('id')

        footer.delete()

        self.assertEquals(self.model.objects.count(), 0)


# **************************************************************************** #
#                                Views test                                    #
# **************************************************************************** #

class ViewsTest(TestCase):
    def setUp(self):
        settings.APPEND_SLASH = False
        self.url = reverse('index')

        Presentation.objects.create(
            title = "Romutech AI",
            description = "Romutech AI est une solution basée sur l'intelligence artificielle.",
            features = [
                {
                    "title": "Détection de visage",
                    "content": "La solution permet de detecter des visages."
                },
                {
                    "title": "Floutage des visages.",
                    "content": "La solution permet d'automatiser le floutage des visages sur une photo."
                }
            ]
        )
        Application.objects.create(title="Lancer L'application Romutech AI", button="Romutech AI")
        Api.objects.create(title="L'API", description="Une API est mise à disponibilité des développeurs.")
        Documentation.objects.create(
            title = "Documentation de l'API",
            description = "Une documentation est disponible. Vous y trouverez les différentes routes existantes, etc.",
            button = "Documentation"
        )
        Footer.objects.create(content="© Romutech | 2021")

    def test_index_view(self):
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')


    def test_404_view(self):
        response = self.client.get("page_that_does_not_exist")

        self.assertEquals(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'menu.html')
        self.assertTemplateUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
