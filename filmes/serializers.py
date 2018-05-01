from rest_framework import serializers
from filmes.models import Filme, Actor, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'age','filme')

class FilmeSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.HyperlinkedIdentityField(view_name='filme-owner', format='html')
    actors = ActorSerializer(many=True ,required=False)

    class Meta:
        model = Filme
        fields = ('url', 'id','title','original_title', 'slug',
                  'synopsis', 'duration_in_seconds', 'image', 'likes', 'published','owner','actors')

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    original_title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    slug = serializers.CharField(max_length=100)
    synopsis = serializers.CharField(max_length=200)
    duration_in_seconds = serializers.IntegerField()
    image = serializers.CharField(max_length=500)
    published = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Filme.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.original_title = validated_data.get('original_title', instance.original_title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.synopsis = validated_data.get('synopsis', instance.synopsis)
        instance.duration_in_seconds = validated_data.get('duration_in_seconds', instance.duration_in_seconds)
        instance.image = validated_data.get('image', instance.image)
        instance.published = validated_data.get('published',instance.published) 

        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    filme = serializers.HyperlinkedRelatedField(many=True, view_name='filme-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'filme')

