from multiprocessing.connection import Client
from unicodedata import name
from urllib import request, response
from django.test import TestCase, Client
from lta.models import Link, User
from lta.views import *
from django.urls import reverse


class ModelTest(TestCase):

    def setUp(self):

        # create the links
        link1 = Link.objects.create(
            name="Twitter", url="https://twitter.com/jude_olowo/")

        # creating a user
        user1 = User.objects.create(
            username="user1", email="user1@gmail.com", bio="Test user", profile_image="default")

    def test_home_page(self):
        links = Link.objects.all()
        self.assertEqual(links.count(), 1)

        c = Client()
        response = c.get(reverse("home"))
        self.assertEqual(response.status_code, 302)

    def test_home_page_link_name(self):
        link1 = Link.objects.get(id=1)
        self.assertTrue(link1.name, "Twitter")

    # testing the preview page

    def test_preview(self):
        links = Link.objects.all()
        self.assertEqual(links.count(), 1)

    def test_preview_username(self):
        user = User.objects.get(username="user1")
        self.assertEqual(user.username, "user1")

        # c = Client()
        # response = c.get(reverse("preview"))
        # self.assertEqual(response.status_code, 200)

        # testing the addlink page
    def test_register_page(self):
        c = Client()
        response = c.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

   # testing the update link page

    def test_update_link_page(self):
        link1 = Link.objects.get("id=1")

        c = Client()
        response = c.get(f"/update-link/{link1.id}")
        self.assertEqual(response.status_code, 200)
