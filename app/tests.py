from django.test import TestCase, Client
from app.models import *
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        user = User(name='asan', age=20)
        user.save()

    def test_age(self):
        user = User.objects.filter(name='asan')
        self.assertEqual(len(user), 1)
        self.assertEqual(user[0].age, 20)

    def test_api(self):
        c = Client()
        res = c.get('/')

        self.assertEqual(res.status_code, 200)
        self.assertTrue('fu' in res.content.decode('utf-8'))

    def test_name(self):
        user = User.objects.filter(name='asan')
        self.assertEqual(len(user), 1)
        self.assertEqual(user[0].name, 'asan')
