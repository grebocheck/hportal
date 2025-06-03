from django.contrib import admin
from .models import Article, Review, Bookmark


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "slug", "user", "createdAt", "featured"]


admin.site.register([Review, Bookmark])
