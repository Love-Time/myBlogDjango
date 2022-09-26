from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class AdminNews(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'cat_id', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100"')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_photo', 'cat_id', 'post_id')
    list_display_links = ('id', 'get_photo')
    search_fields = ('cat_id', 'news_id')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100"')


admin.site.register(News, AdminNews)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
