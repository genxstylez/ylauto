from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'ylauto.views.home', name='home'),
    url(r'^$', 'ylauto.views.index', name='index'),
    url(r'^locale/$', 'ylauto.views.locale', name='locale'),
    
    (r'^grappelli/', include('grappelli.urls')),
    # url(r'^ylauto/', include('ylauto.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'^home/$', 'ylauto.views.home', name='home'),
    url(r'^about/', 'general.views.about', name='about'),
    url(r'^news/', include('news.urls')),
    url(r'^product/', include('product.urls')),
)
