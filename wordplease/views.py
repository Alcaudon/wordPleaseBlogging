from django.shortcuts import render
from wordplease.models import Post

def home(request):
    posts = Post.objects.all().order_by("-date")[:5]
    context = {'posts': posts}
    return render(request, "home.html", context)

def post_detail(request, pk):
    possible_posts = Post.objects.filter(pk=pk).select_related('category')
    if len(possible_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post = possible_posts[0]
        context = {'post': post}
        return render(request, "post_detail.html", context)
