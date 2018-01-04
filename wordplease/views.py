from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from wordplease.forms import PostForm
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

class CreatePostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})

    def post (self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_name", args=[post.pk])
            message = "Post created successfully! "
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})

