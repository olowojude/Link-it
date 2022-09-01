from multiprocessing.connection import Client
from unicodedata import name
from urllib import request, response
from django.test import TestCase
from lta.models import Link, User
from lta.views import *


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
        response = c.get("/home/")
        self.assertEqual(response.status_code, 200)

    def test_home_name(self):
        link1 = Link.objects.get(id=1)
        self.assertTrue(link1.name, "Twitter")

    # testing the preview page

    def test_preview(self):
        links = Link.objects.all()
        self.assertEqual(links.count(), 1)

    def test_preview_username(self):
        user = User.objects.get(username="user1")
        self.assertEqual(user.username, "user1")

        # username = User.objects.get(name="user1")
        # self.assertEqual(username.name, "user1")

        # u = User.objects.get(name="user1")
        # self.assertTrue(u.name, "user1")
