from django.contrib import admin

from wordplease.models import Category, Post

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'introduction', 'date', 'user_full_name', 'category')
    list_filter = ('user', 'category')
    search_fields = ('title', 'introduction')

    def user_full_name(self, obj):
        return "{0} {1}".format(obj.user.first_name, obj.user.last_name)
    user_full_name.short_description = "Post owner"
    user_full_name.admin_order_field = "user__first_name"