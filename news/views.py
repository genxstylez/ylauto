from django.shortcuts import render, get_object_or_404
from news.models import News

def news_list(request):
    news_list = News.objects.order_by('-created_at')
    return render(request, 'news/news-list.html', {'news': news_list})

def news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news/news.html', {'news': news})
