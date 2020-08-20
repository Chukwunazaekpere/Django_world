from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class TestModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email='dht@fg.com',
            password='dht456'
        )

        self.user2 = User.objects.create_user(
            email='dhrt@fg.com',
            password='dht456'
        )

    def test_User_model_saves_new_users(self):
        self.assertEquals(User.objects.count(), 2)

    def test_User_model_fields(self):
        email_field_title = self.user1._meta.get_field('email').verbose_name
        self.assertTrue(email_field_title == 'email')




