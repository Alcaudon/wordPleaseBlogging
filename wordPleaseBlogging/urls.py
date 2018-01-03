from django.contrib import admin
from django.urls import path
from wordplease.views import home, post_detail
from users.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_page"),
    path('posts/<int:pk>', post_detail, name="post_detail_name"),
    path('login', LoginView.as_view(), name='login_page'),
    path('logout', LogoutView.as_view(), name='logout_page')
]
