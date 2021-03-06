from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from wordplease.forms import PostForm
from wordplease.models import Post


def home(request):
    today = timezone.now()
    posts = Post.objects.all().filter(date__lt=today).order_by("-date")[:10]
    context = {'posts': posts}
    return render(request, "home.html", context)


def post_detail(request, username, pk):
    possible_posts = Post.objects.filter(user__username=username, pk=pk).select_related('category')
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
            url = reverse("post_detail_name", args=[post.user.username, post.pk])
            message = "Post created successfully! "
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})


class MyPostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "my_posts.html"

    def get_queryset(self):
        queryset = super(MyPostView, self).get_queryset()
        return queryset.filter(user=self.request.user, date__lte=timezone.now()).order_by('-date')

class PostsByUserName(ListView):

    model = Post
    template_name = 'posts_by_user.html'

    def get_queryset(self):
        queryset = super(PostsByUserName, self).get_queryset()
        username = self.kwargs.get('username')
        return queryset.filter(user__username=username, date__lte=timezone.now()).order_by('-date')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        context['blog'] = user
        return context


