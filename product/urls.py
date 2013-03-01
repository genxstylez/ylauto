from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('product.views',
    url(r'^categories/$', 'categories', name='categories'),
    url(r'^model/(?P<model_id>\d+)/$', 'model', name='model'),
)
