from rest_framework.urlpatterns import format_suffix_patterns
from filmes import views
from django.urls import include, path


urlpatterns = [
    path('filmes/', views.FilmeShowView.as_view(), name='filme-list'),
    path('filmes/findAllOrderBy', views.FilmeListOrderBy.as_view(), name='filme-list-order'),
    path('filmes/likeMovie/<int:pk>', views.filme_like_movie, name='filme-like'),
    path('filmes/likeMovie/<slug:slug>',views.filme_like_movie_slug, name='filme-like-slug'),
    path('filmes/<int:pk>/', views.FilmeDetail.as_view(), name='filme-detail'),
    path('filmes/<slug:slug>/', views.FilmeDetailSlug.as_view(), name='filme-slug'),
    path('filmes/<int:pk>/owner/', views.FilmeOwner.as_view(), name='filme-owner'),
    path('actors/', views.ActorShowView.as_view(), name='actor-list'),
    path('actors/<int:pk>', views.ActorShowDetail.as_view(), name='actor-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
]
