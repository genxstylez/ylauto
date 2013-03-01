from django.shortcuts import render
from general.models import About

def about(request):
    about = About.objects.order_by('-id')[0]
    return render(request, 'general/about.html', {'about': about})
