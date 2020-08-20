from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        pass

    def test_SignUpView(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEquals(response.status_code, 200)

    def test_SignupView_TemplateUsed(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_SignupForm_save_method(self):
        data = {
                'email': 'sdgx@sd.com',
                'password1': 'trdssdfg64ui7644sj',
                'password2': 'trdssdfg64ui7644sj'
            }
        response = self.client.post(reverse('accounts:signup'), data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.count(), 1)

        self.assertTrue(User.objects.get(email=data['email']))


