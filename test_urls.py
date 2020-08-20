from django.test import TestCase, RequestFactory

from django.urls import resolve, reverse
from ..views import SignUpView


class TestUrls(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_signup_url(self):
        request  = resolve('/shop/accounts/signup/')

        self.assertTrue(request.func.__name__ == "SignUpView")

    def test_signup_url_view_name(self):
        request  = resolve('/shop/accounts/signup/')

        self.assertEquals(request.view_name, "accounts:signup")

    def test_login_view_name(self):
        request = resolve('/shop/accounts/login/')
        self.assertEquals(request.func.__name__, "LoginView")

    def test_login_url_view_name(self):
        request  = resolve('/shop/accounts/login/')

        self.assertTrue(request.view_name == "accounts:login")
