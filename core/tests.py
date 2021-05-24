from django.test import TestCase
from .models import Post, Comment, Like, Follow
from user.models import User


# Create your tests here.
class TestPostClass(TestCase):
    """
    Test class that test posts objects
    """

    def setUp(self) -> None:
        self.new_user = User(picture='default.png', full_name='Paul Ngigi', email='paul@ngigi.com')
        self.new_post = Post(user=User, image='default.png', caption='cool pic')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))
