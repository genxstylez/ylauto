from django.shortcuts import render
from general.models import About
import re

def about(request):
    about = About.objects.order_by('-id')[0]
    return render(request, 'general/about.html', {'about': about})

def contact(request):
    path = request.path
    template = 'general/contact.html'
    if '/zh-cn' in path:
        match = re.match('/zh-cn(.+)', path)
        path = match.groups()[0]
        template = 'general/contact-cn.html'
 
    return render(request, template)
