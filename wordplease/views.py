from django.shortcuts import render
from wordplease.models import Post

def home(request):
    posts = Post.objects.all().order_by("-date")[:5]
    context = {'posts': posts}
    return render(request, "home.html", context)

