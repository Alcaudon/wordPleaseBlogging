from django.contrib import admin
from django.urls import path
from wordplease.views import home, post_detail
from users.views import login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_page"),
    path('posts/<int:pk>', post_detail, name="post_detail_name"),
    path('login', login, name='login_page')
]
