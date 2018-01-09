from django.contrib import admin
from django.urls import path
from wordplease.views import home, post_detail, CreatePostView, MyPostView
from users.views import LoginView, LogoutView, Blogs


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', MyPostView.as_view(), name="my_posts_page"),
    path('blogs/<str:user_name>/', PostsUserView.as_view(), name='posts_by_user'),

    path('login', LoginView.as_view(), name='login_page'),
    path('logout', LogoutView.as_view(), name='logout_page'),

    path('post/crear', CreatePostView.as_view(), name="create_post_page"),

    path('blogs/', Blogs.as_view(), name="blogs_page"),
    path('posts/<int:pk>', post_detail, name="post_detail_name"),
    path('', home, name="home_page"),

]
