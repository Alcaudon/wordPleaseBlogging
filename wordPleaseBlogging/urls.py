from django.contrib import admin
from django.urls import path
from wordplease.views import home, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_page"),
    path('posts/<int:pk>', post_detail, name="post_detail_name")
]
