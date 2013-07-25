from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('gallery.views',
    url(r'^$', 'gallery_list', name='gallery-list'),
    url(r'^(?P<gallery_id>\d+)/$', 'gallery_view', name='gallery'),
)
