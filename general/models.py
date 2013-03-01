from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
import uuid

class About(models.Model):
    def about_path(self, filename):
        return 'about/about.%s' % filename.split('.')[1]
    content = models.TextField(_('content'))
    image = ThumbnailerImageField(_('image'), upload_to=about_path, resize_source=dict(size=(960, 0), sharpen=True))

class ImageSlide(models.Model):
    def slides_path(self, filename):
        return 'slides/%s.%s' % (uuid.uuid4(), filename.split('.')[1])

    image = ThumbnailerImageField(_('image'), upload_to=slides_path, resize_source=dict(size=(960, 0), sharpen=True))
    active = models.BooleanField(_('active'), default=True)
