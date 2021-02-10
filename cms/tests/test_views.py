from django.test import TestCase
from cms.models import Presentation, Application, Api, Documentation, Footer
from django.urls import reverse


class ViewsTest(TestCase):
    def setUp(self):
        self.url = reverse('index')

        self.presentation = Presentation.objects.create(
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
        self.application = Application.objects.create(title="Lancer L'application Romutech AI", button="Romutech AI")
        self.api = Api.objects.create(title="L'API", description="Une API est mise à disponibilité des développeurs.")
        self.documentation = Documentation.objects.create(
            title = "Documentation de l'API",
            description = "Une documentation est disponible. Vous y trouverez les différentes routes existantes, etc.",
            button = "Documentation"
        )
        self.footer = Footer.objects.create(content="© Romutech | 2021")


    def test_index_view(self):
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
        self.assertEquals(response.context['presentation'], self.presentation)
        self.assertEquals(response.context['application'], self.application)
        self.assertEquals(response.context['api'], self.api)
        self.assertEquals(response.context['documentation'], self.documentation)
        self.assertEquals(response.context['footer'], self.footer)


    def test_404_view(self):
        response = self.client.get("page_that_does_not_exist")

        self.assertEquals(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'menu.html')
        self.assertTemplateUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
