from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text = "This is a test!")
    
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_name_at_loc(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_exists_at_correct_loc(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    
    def text_check_the_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def text_content_with_db(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")

