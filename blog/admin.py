from django.contrib import admin
from django.db import models
from .models import Article, Category, Tag
from mdeditor.widgets import MDEditorWidget
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name'] 

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name'] 

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'category', 'modified_time', 'author']
    search_fields = ['title', 'category', 'tags', 'author']
    list_filter = ['title', 'category', 'tags', 'author']

    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)