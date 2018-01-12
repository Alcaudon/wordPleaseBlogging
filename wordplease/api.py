from rest_framework.response import Response
from rest_framework.views import APIView

from wordplease.models import Post
from wordplease.serializers import PostSerializer


class PostListAPI(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
