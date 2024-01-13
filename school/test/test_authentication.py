from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthenticationTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('test', password='12345')

    def test_user_authentication(self):
        user = authenticate(username=self.user.username, password=self.user.password)
        self.assertTrue(user is not None)
