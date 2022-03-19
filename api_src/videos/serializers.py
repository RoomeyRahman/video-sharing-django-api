from rest_framework import serializers
from .models import Video
from django.contrib.auth.models import User


class VideoSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Video
        fields = ('id', 'title', 'slug', 'description', 'creator', 'url', 'thumbnail_url')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    videos = serializers.PrimaryKeyRelatedField(many=True, queryset=Video.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'videos')