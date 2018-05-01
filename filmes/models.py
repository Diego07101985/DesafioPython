from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Filme(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    original_title = models.CharField(max_length=100, blank=True, default='')
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    synopsis = models.TextField()
    duration_in_seconds = models.IntegerField()
    image = models.ImageField()
    likes = models.IntegerField()
    published = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='filmes', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Actor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    age = models.IntegerField()
    filme = models.ForeignKey(to=Filme, related_name="actors", on_delete= models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('created',)

