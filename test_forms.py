from django.test import TestCase, RequestFactory
from ..forms import SignupForm

from django.urls import resolve
from ..views import SignUpView

from django.contrib.auth import get_user_model
User = get_user_model()
from django.core import mail


class TestForms(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.form = SignupForm(
            {
                'email': 'sdgx@sd.com',
                'password1': 'trdssdfg64ui7644sj',
                'password2': 'trdssdfg64ui7644sj'
            }
        )

        self.form_details = {
            'email': 'sdgx@sd.com',
            'password1': 'trdssdfg64ui7644sj',
            'password2': 'trdssdfg64ui7644sj'
        }

    def test_form_validity(self):
        self.assertTrue(self.form.is_valid())

    def test_SignupForm_save_method(self):
        request = self.factory.get('shop/accounts/signup/')
        response = SignUpView.as_view()(request, {
                'email': 'sdgx@sd.com',
                'password1': 'trdssdfg64ui7644sj',
                'password2': 'trdssdfg64ui7644sj'
            })
        # self.form.save(request)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.count(), 2)
