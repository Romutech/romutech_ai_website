from django.test import TestCase
from cms.models import Presentation, Application, Api, Documentation, Footer
from django.urls import reverse


class ViewsTest(TestCase):
    def setUp(self):
        self.url = reverse('index')

        self.presentation = {
            'title': "Romutech AI",
            'description': "Romutech AI est une solution basée sur l'intelligence artificielle.",
            'features': [
                {
                    "title": "Détection de visage",
                    "content": "La solution permet de detecter des visages."
                },
                {
                    "title": "Floutage des visages.",
                    "content": "La solution permet d'automatiser le floutage des visages sur une photo."
                }
            ]
        }
        self.application = {'title': "Lancer L'application Romutech AI", 'button': "Romutech AI"}
        self.api = {'title': "L'API", 'description': "Une API est mise à disponibilité des développeurs."}
        self.documentation  = {
            'title': "Documentation de l'API",
            'description': "Une documentation est disponible. Vous y trouverez les différentes routes existantes, etc.",
            'button': "Documentation"
        }
        self.footer = {'content': "© Romutech | 2021"}


    def test_index_view(self):
        Presentation.objects.create(
            title=self.presentation['title'],
            description=self.presentation['description'],
            features=self.presentation['features']
        )
        Application.objects.create(title=self.application['title'], button=self.application['button'])
        Api.objects.create(title=self.api['title'], description=self.api['description'])
        Documentation.objects.create(
            title=self.documentation['title'],
            description=self.documentation['description'],
            button=self.documentation['button']
        )
        Footer.objects.create(content=self.footer['content'])

        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'modal.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
        self.assertIn('presentation', response.context)
        self.assertIn('application', response.context)
        self.assertIn('api', response.context)
        self.assertIn('documentation', response.context)
        self.assertIn('footer', response.context)


    def test_index_view_without_presentation(self):
        Application.objects.create(title=self.application['title'], button=self.application['button'])
        Api.objects.create(title=self.api['title'], description=self.api['description'])
        Documentation.objects.create(
            title=self.documentation['title'],
            description=self.documentation['description'],
            button=self.documentation['button']
        )
        Footer.objects.create(content=self.footer['content'])

        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'modal.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
        self.assertNotIn('presentation', response.context)
        self.assertIn('application', response.context)
        self.assertIn('api', response.context)
        self.assertIn('documentation', response.context)
        self.assertIn('footer', response.context)


    def test_index_view_without_application(self):
        Presentation.objects.create(
            title=self.presentation['title'],
            description=self.presentation['description'],
            features=self.presentation['features']
        )
        Api.objects.create(title=self.api['title'], description=self.api['description'])
        Documentation.objects.create(
            title=self.documentation['title'],
            description=self.documentation['description'],
            button=self.documentation['button']
        )
        Footer.objects.create(content=self.footer['content'])

        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'modal.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
        self.assertIn('presentation', response.context)
        self.assertNotIn('application', response.context)
        self.assertIn('api', response.context)
        self.assertIn('documentation', response.context)
        self.assertIn('footer', response.context)


    def test_index_view_without_api(self):
        Presentation.objects.create(
            title=self.presentation['title'],
            description=self.presentation['description'],
            features=self.presentation['features']
        )
        Application.objects.create(title=self.application['title'], button=self.application['button'])
        Documentation.objects.create(
            title=self.documentation['title'],
            description=self.documentation['description'],
            button=self.documentation['button']
        )
        Footer.objects.create(content=self.footer['content'])

        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'modal.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
        self.assertIn('presentation', response.context)
        self.assertIn('application', response.context)
        self.assertNotIn('api', response.context)
        self.assertIn('documentation', response.context)
        self.assertIn('footer', response.context)


    def test_index_view_without_documentation(self):
        Presentation.objects.create(
            title=self.presentation['title'],
            description=self.presentation['description'],
            features=self.presentation['features']
        )
        Application.objects.create(title=self.application['title'], button=self.application['button'])
        Api.objects.create(title=self.api['title'], description=self.api['description'])
        Footer.objects.create(content=self.footer['content'])

        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'modal.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
        self.assertIn('presentation', response.context)
        self.assertIn('application', response.context)
        self.assertIn('api', response.context)
        self.assertNotIn('documentation', response.context)
        self.assertIn('footer', response.context)


    def test_index_view_without_footer(self):
        Presentation.objects.create(
            title=self.presentation['title'],
            description=self.presentation['description'],
            features=self.presentation['features']
        )
        Application.objects.create(title=self.application['title'], button=self.application['button'])
        Api.objects.create(title=self.api['title'], description=self.api['description'])
        Documentation.objects.create(
            title=self.documentation['title'],
            description=self.documentation['description'],
            button=self.documentation['button']
        )

        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'modal.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
        self.assertIn('presentation', response.context)
        self.assertIn('application', response.context)
        self.assertIn('api', response.context)
        self.assertIn('documentation', response.context)
        self.assertNotIn('footer', response.context)


    def test_index_view_with_no_data(self):
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'modal.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateNotUsed(response, 'menu.html')
        self.assertTemplateNotUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
        self.assertNotIn('presentation', response.context)
        self.assertNotIn('application', response.context)
        self.assertNotIn('api', response.context)
        self.assertNotIn('documentation', response.context)
        self.assertNotIn('footer', response.context)


    def test_404_view(self):
        response = self.client.get("page_that_does_not_exist")

        self.assertEquals(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'cms/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'menu.html')
        self.assertTemplateUsed(response, '404.html')
        self.assertTemplateNotUsed(response, '500.html')
