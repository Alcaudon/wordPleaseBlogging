from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from wordplease.forms import PostForm
from wordplease.models import Post

@login_required
def home(request):
    posts = Post.objects.all().order_by("-date")[:5]
    context = {'posts': posts}
    return render(request, "home.html", context)

@login_required
def post_detail(request, pk):
    possible_posts = Post.objects.filter(pk=pk).select_related('category')
    if len(possible_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post = possible_posts[0]
        context = {'post': post}
        return render(request, "post_detail.html", context)


class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})

    def post (self, request):
        post = Post()
        post.user = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_name", args=[post.pk])
            message = "Post created successfully! "
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})


class MyPostView(LoginRequiredMixin, ListView):

    model = Post
    template_name = "my_posts.html"

    def get_queryset(self):
        queryset = super(MyPostView, self).get_queryset()
        return queryset.filter(user=self.request.user)
