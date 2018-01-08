from django.contrib import admin
from django.utils.safestring import mark_safe

from wordplease.models import Category, Post

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'introduction', 'date', 'user_full_name', 'category')
    list_filter = ('user', 'category')
    search_fields = ('title', 'introduction')

    def user_full_name(self, post):
        return "{0} {1}".format(post.user.first_name, post.user.last_name)
    user_full_name.short_description = "Post owner"
    user_full_name.admin_order_field = "user__first_name"

    def get_image_html(self, post):
        return mark_safe('<img src="{0}" alt="{1}" height="100">'.format(post.URL, post.title))
    get_image_html.short_description = "Post image"

    readonly_fields = ('get_image_html',)
    fieldsets = (
        (None, {
            'fields':('title', 'introduction')
        }),
        ("Body, URL photo and date ", {
            'fields': ('body', 'get_image_html', 'URL', 'date')
        }),
        ("User and Category", {
            'fields': ('user', 'category'),
            'classes':('collapse',),
            'description': 'Foreign keys'
        })
    )