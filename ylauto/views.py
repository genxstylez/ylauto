from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from product.models import Category
from news.models import News

def index(request):
    return render(request, 'index.html')

def home(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'news': news, 'categories': categories})

def locale(request):
    path = request.GET.get('path', '')
    locale = request.GET.get('locale', 'zh-tw')
    activate(locale)
    if path:
        return redirect('/%s%s' % (locale, path))
    else:
        return redirect(reverse('home'))
