# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

class Gallery(models.Model):
    def gallery_cover_path(self, filename):
        filename = filename.encode('utf-8')
        return 'gallery/cover/%s' % filename
    cover = ThumbnailerImageField(_('cover'), upload_to=gallery_cover_path, resize_source=dict(size=(150, 58), sharpen=True))
    title = models.CharField(_('title'), max_length=50)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)

class GalleryItem(models.Model):
    def gallery_path(self, filename):
        filename = filename.encode('utf-8')
        return 'gallery/%s/%s.%s' % (self.gallery.id, filename.split('.')[0], filename.split('.')[-1])

    gallery = models.ForeignKey(Gallery, related_name='items')
    image = models.ImageField(_('image'), upload_to=gallery_path)
