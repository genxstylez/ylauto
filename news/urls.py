from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('news.views',
    url(r'^$', 'news_list', name='news-list'),
    url(r'^(?P<news_id>\d+)/$', 'news', name='news'),
)
