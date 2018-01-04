from django.contrib import admin
from django.urls import path
from wordplease.views import home, post_detail, CreatePostView
from users.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', LoginView.as_view(), name='login_page'),
    path('logout', LogoutView.as_view(), name='logout_page'),

    path('post/crear', CreatePostView.as_view(), name="create_post_page"),

    path('', home, name="home_page"),
    path('posts/<int:pk>', post_detail, name="post_detail_name")
]
