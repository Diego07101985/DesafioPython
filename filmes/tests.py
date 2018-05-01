from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from filmes.models import Filme, Actor
from rest_framework.test import APIClient
from django.contrib.auth.models import User

import logging
logger = logging.getLogger('desafio')


class FilmeTests(APITestCase):
    
    username = 'admin'
    password = '12345'
    movie = ''

    def setUp(self):
        User.objects.create_superuser(
            username=self.username,
            password=self.password,
            email='teste@teste.com',
            is_superuser=True,
            is_staff=True
        )   
        self.movie = {
            'title': 'Novo filme',
            'original_title': 'Novo filme',
            'slug': 'teste',
            'synopsis': 'Teste de criacao',
            'duration_in_seconds': 100000,
            'image': 'https://minilua.com/verdadeira-historia-massacre-serra-eletrica/',
            'likes':9,
            'published': True,
            'owner':'admin'
        } 

    
    def test_create_movie(self):
        url = reverse('filme-list')
        self.assertEqual(User.objects.get(pk=1).username, self.username)
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.post(url, self.movie, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Filme.objects.get().title, self.movie['title'])

   # def test_increment_like_movie(self):
   #     url = reverse('filme-like')
        
  #  def test_increment_like_movie_slug(self):
  #      url = reverse('filme-like-slug')
    

    def test_update_filme(self):
        self.test_create_movie()
        new_filme = {
            "title": "Exemplo1",
            "original_title": "Exemplo1",
            "slug": "exemplo-slug1",
            "synopsis": "Exempo test1",
            "duration_in_seconds": 100000,
            "image": "https://minilua.com/verdadeira-historia-massacre-serra-eletrica/",
            "likes":9,
            "published": True,
            "owner":"admin"
        } 
        self.assertEqual(User.objects.get(pk=1).username, self.username)
        filme = Filme.objects.get(title=self.movie['title'])
        url_movie = "/filmes/"+str(filme.id)+"/"

        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.put(url_movie,new_filme, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Filme.objects.get().title, 'Exemplo1')


    def test_update_movie_slug(self):
        self.test_create_movie()

        new_filme = {
            "title": "Exemplo1",
            "original_title": "Exemplo1",
            "slug": "exemplo-slug1",
            "synopsis": "Exempo test1",
            "duration_in_seconds": 100000,
            "image": "https://minilua.com/verdadeira-historia-massacre-serra-eletrica/",
            "likes":9,
            "published": True,
            "owner":"admin"
        } 

        self.assertEqual(User.objects.get(pk=1).username, self.username)
        filme = Filme.objects.get(title=self.movie['title'])
        url_movie = '/filmes/'+filme.slug+"/"

        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.put(url_movie,new_filme, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Filme.objects.get().title,new_filme['title'])


    def test_delete_movie(self):

        self.test_create_movie()
        filme = Filme.objects.get(title=self.movie['title'])
        url_movie = "/filmes/"+str(filme.id)+"/"

        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.delete(url_movie,self.movie,format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url_movie)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



   # def test_create_actor_and_save_in_movie(self):
    #    url_actor = reverse('actor-list')
    #    url_filme = reverse('filme-list')

        

class ActorTests(APITestCase):

    username = 'admin'
    password = '12345'
    actor = {}
    filme = {}

    def setUp(self):
        User.objects.create_superuser(
            username=self.username,
            password=self.password,
            email='teste@teste.com',
            is_superuser=True,
            is_staff=True
        )

        self.actor = {
            'id': 1,
            'name': 'Paulo',
            'age': 22 
        }       
        
    
    def test_create_actor(self):
        url_actor = reverse('actor-list')

        self.assertEqual(User.objects.get(pk=1).username, self.username)
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.post(url_actor, self.actor, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.get().name, self.actor['name'])


    def test_update_actor(self):
        new_actor = {
            "name": "Paulo",
            "age": 18
        }

        self.test_create_actor()

        url_actor = "/actors/"+str(self.actor['id'])+"/"
        print(url_actor)
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.put(url_actor,new_actor, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(Actor.objects.get().age,self.actor['age'])

        
   # def test_delete_actor(self):
   #     url_actor = reverse('actor-detail')
