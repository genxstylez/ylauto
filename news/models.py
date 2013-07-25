# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

class News(models.Model):
    def news_image_path(self, filename):
        return 'news/%s/image.%s' % (self.pk, filename.split('.')[1])

    class Meta:
        verbose_name_plural = 'News'

    def __unicode__(self):
        return self.title

    title = models.CharField(_('title'), max_length=50)
    content = models.TextField(_('content'))
    image = ThumbnailerImageField(_('image'), upload_to=news_image_path)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)

