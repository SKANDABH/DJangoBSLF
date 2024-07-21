from django.contrib import admin

from .models import Category, BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'is_draft')
    list_filter = ('category', 'author', 'is_draft')
    search_fields = ('title', 'content')


admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)
