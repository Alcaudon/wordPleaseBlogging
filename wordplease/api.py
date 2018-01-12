from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from wordplease.models import Post
from wordplease.serializers import PostSerializer


class PostListAPI(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer