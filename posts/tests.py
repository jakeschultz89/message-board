from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModeTest(TestCase):
    def setUp(self):
        Post.objects.create(title="test", body="case")

    def test_post_title(self):
        post = Post.objects.get(id=1)
        expected_obj_name = f"{post.title}"
        self.assertEqual(expected_obj_name, "test")

class PostListViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="this is a test", body="whatever")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/posts/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_contains_correct_data(self):
        resp = self.client.get("/posts/")
        self.assertContains(resp, "this is a test")

    def test_view_url_contains_correct_templates(self):
        resp = self.client.get("/posts/")
        self.assertTemplateUsed(resp, "post_list.html")
        self.assertTemplateUsed(resp, "base.html")

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("post_list"))
        self.assertEqual(resp.status_code, 200)

class PostDetailViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="this is a test", body="whatever")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/posts/1/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_contains_correct_data(self):
        resp = self.client.get("/posts/1/")
        self.assertContains(resp, "this is a test")

    def test_view_url_contains_correct_templates(self):
        resp = self.client.get("/posts/1/")
        self.assertTemplateUsed(resp, "post_detail.html")
        self.assertTemplateUsed(resp, "base.html")

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("post_detail", args=[1]))
        self.assertEqual(resp.status_code, 200)