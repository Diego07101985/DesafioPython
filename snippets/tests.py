from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from snippets.models import Snippet
from rest_framework.test import APIClient
from django.contrib.auth.models import User

import logging
logger = logging.getLogger('desafio')



class AccountTests(APITestCase):
    
    username = 'admin'
    password = '12345'

    def setUp(self):
        User.objects.create_superuser(
            username=self.username,
            password=self.password,
            email='demo@demo.com',
            is_superuser=True,
            is_staff=True
        )
    
    def test_create_account(self):
        url = reverse('snippet-list')

    
        data = {
            "owner": "disalles7",
            "title": "BeloTeste",
            "code": "print 934",
            "linenos": False,
            "language": "python",
            "style": "friendly"
        }
        self.assertEqual(User.objects.get(pk=1).username, self.username)
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.get().title, 'BeloTeste')

