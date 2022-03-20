from rest_framework import serializers
from .models import Video
from django.contrib.auth.models import User


# create class to serializer model
class VideoSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Video
        fields = ('id', 'title', 'slug', 'description',
                  'creator', 'url', 'thumbnail_url')


# create class to serializer user model
class UserSerializer(serializers.ModelSerializer):
    videos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Video.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'videos')
