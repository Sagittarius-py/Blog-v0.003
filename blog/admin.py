from django.contrib import admin
from .models import Post, PostImage
from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'content')
    list_filter = ("status", 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Post, PostAdmin)
