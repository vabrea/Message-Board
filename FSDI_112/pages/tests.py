from django.test import SimpleTestCase
from django.urls import reverse

class SimplePageTest(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_templates(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "index.html")

    def test_about_page_uses_correct_templates(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "about.html")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_home_page_contans_correct_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "My Django App")

    def test_about_page_contains_correct_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "About Von Abrea")