from django.test import TestCase
from .models import User


# Create your tests here.
class TestUserClass(TestCase):
    def setUp(self) -> None:
        self.new_user = User(picture='default.png', full_name='Paul Ngigi', email='paul@ngigi.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))
