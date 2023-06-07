from django.contrib.auth import get_user_model
from django.test import TestCase
User = get_user_model()


class UserLoginTestCase(TestCase):

    def set_up(self):
        User.objects.create(username='admin', password='aldo', email='qwe@mail.ru')

    def test_login(self):
        self.set_up()
        result = self.client.post('farabi-admin/login', {'username': 'admin', 'password': 'aldo'})
        return result