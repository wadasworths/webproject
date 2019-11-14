from django import template
from ..models import Article, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=7):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_tags():
    return Tag.objects.all()

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('article'))