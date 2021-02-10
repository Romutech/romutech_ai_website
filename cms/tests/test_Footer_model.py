from django.test import TestCase
from cms.models import Footer


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