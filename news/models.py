from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

class News(models.Model):
    def news_thumb_path(self, filename):
        return 'news/%s/thumb.%s' % (self.title, filename.split('.')[1])
    def news_image_path(self, filename):
        return 'news/%s/image.%s' % (self.title, filename.split('.')[1])
    class Meta:
        verbose_name_plural = 'News'

    title = models.CharField(_('title'), max_length=50)
    thumb = ThumbnailerImageField(_('thumb'), upload_to=news_thumb_path, resize_source=dict(size=(100, 0), crop='scale', sharpen=True))
    image = ThumbnailerImageField(_('image'), upload_to=news_image_path, resize_source=dict(size=(900, 0), crop='scale', sharpen=True))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)
