from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import include, path


urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<slug:title>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('snippets/<int:pk>/owner/', views.SnippetOwner.as_view(), name='snippet-owner'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
]
