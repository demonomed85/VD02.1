from django.shortcuts import render
from .models import News_post

def news_home(request):
    news = News_post.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

def news_page(request):
    return render(request, 'news/news_page.html')
