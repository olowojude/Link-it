from unicodedata import name
from django.test import TestCase
from lta.models import Link, User


class ModelTest(TestCase):

    def setUp(self):

        # create the links
        link1 = Link.objects.create(
            name="Twitter", url="https://twitter.com/jude_olowo/")

        # creating a user
        user1 = User.objects.create(
            username="user1", email="user1@gmail.com", bio="Test user", profile_image="default")

    def test_link_name(self):
        link1 = Link.objects.get(id=1)
        self.assertTrue(link1.name, "Facebook")

    def test_link_url(self):
        link1 = Link.objects.get(id=1)
        self.assertEqual(link1.url, "https://twitter.com/jude_olowo/")

    # testig the field labels

    def test_name_label(self):
        link1 = Link.objects.get(id=1)
        field_name = Link._meta.get_field("name").verbose_name
        self.assertTrue(field_name, "name")

    def test_url_label(self):
        a = Link.objects.get(id=1)
        field_name = Link._meta.get_field("url").verbose_name
        self.assertTrue(field_name, "url")

    # testing the user model

    def test_user_name(self):
        u = User.objects.get(username="user1")
        self.assertEqual(u.username, "user1")

    def test_username_label(self):
        link1 = User.objects.get(username="user1")
        field_name = User._meta.get_field("username").verbose_name
        self.assertTrue(field_name, "username")

    def test_user_email(self):
        u = User.objects.get(username="user1")
        print(u)
        self.assertTrue(u.email, "user1@gmail.com")

    def test_user_bio(self):
        u = User.objects.get(username="user1")
        self.assertEqual(u.bio, "Test user")

    def test_user_profile_image(self):
        u = User.objects.get(username="user1")
        self.assertTrue(u.profile_image, "avatar.png")
