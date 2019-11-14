from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category, Tag
import markdown

# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/index.html', context={'article_list': articles})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-created_time')
    
    return render(request, 'blog/index.html', context={'article_list': article_list})

def about(request):
   category_list = Category.objects.all()
   return render(request, 'blog/about.html', context={'category_list': category_list})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])

    return render(request, 'blog/detail.html', context={'article': article})


def archives(request):
    dates = Article.objects.datetimes('created_time', 'month', order='DESC')
    article_list = Article.objects.all().order_by('-created_time')
 
    return render(request, 'blog/archives.html', context={'dates' : dates,
                                                        'article_list': article_list})
