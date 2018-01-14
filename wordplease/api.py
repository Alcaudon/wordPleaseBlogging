from django.utils import timezone
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from wordplease.models import Post
from wordplease.permissions import PostPermissions
from wordplease.serializers import PostSerializer, PostsListSerializer, PostUserSerializer


class PostListAPI(ListCreateAPIView):

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter ]
    search_fields = ["title", "body"]
    ordering_fields = ["title", "date"]

    def get_serializer_class(self):
        return PostsListSerializer if self.request.method == "GET" else PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermissions]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostListAPIUser(ListAPIView):

    serializer_class = PostUserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['title', 'date']
    ordering = ('-date',)

    def get_queryset(self):
        user_name = self.kwargs.get('user_name')
        queryset = Post.objects.filter(user__username=user_name)
        user = self.request.user
        if user.username != user_name and not user.is_superuser:
            queryset = queryset.filter(date__lte=timezone.now())
        return queryset
