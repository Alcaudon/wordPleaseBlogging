from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from wordplease.models import Post
from wordplease.serializers import PostSerializer, PostsListSerializer


class PostListAPI(ListCreateAPIView):

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return PostsListSerializer if self.request.method == "GET" else PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)