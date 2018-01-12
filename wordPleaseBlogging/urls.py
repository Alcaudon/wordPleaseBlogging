from django.contrib import admin
from django.urls import path

from users.api import UserListAPI, UserDetailAPI
from wordplease.api import PostListAPI
from wordplease.views import home, post_detail, CreatePostView, MyPostView, PostsByUserName
from users.views import LoginView, LogoutView, Blogs, SignUpView


urlpatterns = [
    path('', home, name="home_page"),
    path('admin/', admin.site.urls),
    path('posts/', MyPostView.as_view(), name="my_posts_page"),
    path('blogs/<str:username>/<int:pk>', post_detail, name="post_detail_name"),

    path('blogs/', Blogs.as_view(), name="blogs_page"),
    path('blogs/<str:username>/', PostsByUserName.as_view(), name="posts_by_name"),


    path('login', LoginView.as_view(), name="login_page"),
    path('logout', LogoutView.as_view(), name="logout_page"),
    path('signup/', SignUpView.as_view(), name="signup"),

    path('new-post/', CreatePostView.as_view(), name="create_post_page"),

    # API REST

    path('api/1.0/users/<int:pk>', UserDetailAPI.as_view(), name="api_user_detail"),
    path('api/1.0/users/', UserListAPI.as_view(), name="api_user_list"),

    path('api/1.0/posts/', PostListAPI.as_view(), name="api_post_list")

]
