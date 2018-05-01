from filmes.models import Filme
from django.conf import settings
from filmes.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from filmes.models import Filme, Actor 
from filmes.serializers import FilmeSerializer, ActorSerializer
from rest_framework import mixins
from rest_framework import generics
from filmes.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.pagination import PageNumberPagination
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from core.mixin import CacheMixin 
from django.core.cache import cache
from rest_framework import status


import logging

logger = logging.getLogger('desafio')

@api_view(['PATCH'])
def filme_like_movie_slug(request, *args, **kwargs):
    logger.info('dentro do metodo filme_like_movie_slug')
    filme = Filme.objects.get(slug=kwargs['slug'])
    if filme is not None:
        filme.likes = filme.likes + 1
        filme.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def filme_like_movie(request, *args, **kwargs):
    logger.info('dentro do metodo filme_like_movie')
    filme = Filme.objects.get(id=kwargs['pk'])
    if filme is not None:
        filme.likes = filme.likes + 1
        filme.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

class FilmeOwner(generics.GenericAPIView):
    queryset = Filme.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        return Response(filme.owner)


class FilmeShowView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    logger.info('Executa filme show view')
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_serializer_class = PageNumberPagination
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        slug = request.data['slug']
        logger.info('dentro do metodo slug = '+slug)
        if self.queryset.filter(slug = slug).exists():
            return Response(status=status.HTTP_409_CONFLICT)
   
        cache.delete_pattern("*filme*")
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        logger.info('Executa o metodo perform_create e faz append user')
        serializer.save(owner=self.request.user)


class FilmeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    def put(self, request, *args, **kwargs):
        slug = request.data['slug']
        if self.queryset.filter(slug = slug).exists():
            return Response(status=status.HTTP_409_CONFLICT)

        logger.info('class FilmeDetail - dentro do metodo PUT reseta cache key filme')
        cache.delete_pattern("*filme*")
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        logger.info('class FilmeDetail - dentro do metodo DELETE reseta cache key filme')
        cache.delete_pattern("*filme*")
        return self.destroy(request, *args, **kwargs)


class FilmeDetailSlug(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    lookup_field = 'slug'

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def put(self, request, *args, **kwargs):
        slug = request.data['slug']
        if self.queryset.filter(slug = slug).exists():
            return Response(status=status.HTTP_409_CONFLICT)

        logger.info('class FilmeDetailSlug - dentro do metodo PUT reseta cache key filme')
        cache.delete_pattern("*filme*")
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        logger.info('class FilmeDetailSlug - dentro do metodo DELETE reseta cache key filme')
        cache.delete_pattern("*filme*")
        return self.destroy(request, *args, **kwargs)

    
class FilmeListOrderBy(CacheMixin, generics.ListAPIView):
    serializer_class = FilmeSerializer
    pagination_serializer_class = PageNumberPagination
    paginate_by = 10
    cache_timeout = 90
    key_prefix = 'filme'
    context_object_name = "filme-list-order"
    
    def get_queryset(self):
        
        type = self.request.GET.get('type', None)
        logger.info('class FilmeListOrderBy - dentro do metodo get_queryset type = '+type)
        qs = Filme.objects.order_by(type)
        
        return qs


class ActorShowView(generics.ListAPIView,
                  generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorShowDetail(generics.RetrieveAPIView,
                        generics.UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
