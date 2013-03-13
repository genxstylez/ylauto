from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from product.models import Category
from news.models import News
from django.http import HttpResponse
from general.models import ImageSlide
import re

def index(request):
    slides = ImageSlide.objects.filter(active=True)
    return render(request, 'index.html', {'slides': slides})

def home(request):
    news = News.objects.all()
    categories = Category.objects.all()
    slides = ImageSlide.objects.filter(active=True)
    return render(request, 'home.html', {'news': news, 'categories': categories, 'slides': slides})

def locale(request):
    path = request.GET.get('path', '')
    locale = request.GET.get('locale', 'zh-tw')
    if path:
        if '/zh-cn' in path:
            match = re.match('/zh-cn(.+)', path)
            path = match.groups()[0]
        if '/zh-tw' in path:
            match = re.match('/zh-tw(.+)', path)
            path = match.groups()[0]
        if '/en' in path:
            match = re.match('/en(.+)', path)
            path = match.groups()[0]
        return redirect('/%s%s' % (locale, path))
    else:
        activate(locale)
        return redirect(reverse('home'))
