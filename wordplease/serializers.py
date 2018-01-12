from rest_framework import serializers

from users.serializers import UserSerializer
from wordplease.models import Post


class PostsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["title", "URL", "introduction", "date"]


class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
