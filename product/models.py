from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))

    def __unicode__(self):
        return self.name


class Make(models.Model):
    name = models.CharField(_('name'), max_length=100)
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='makes')

    def __unicode__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(_('name'), max_length=100)
    make = models.ForeignKey(Make, verbose_name=_('make'), related_name='series')

    class Meta:
        verbose_name_plural = 'Series'

    def __unicode__(self):
        return self.name



class Model(models.Model):
    def off_upload_path(self, filename):
        return 'products/%s/thumb-off.%s' % (self.name, filename.split('.')[1])
    def on_upload_path(self, filename):
        return 'products/%s/thumb-on.%s' % (self.name, filename.split('.')[1])
    name = models.CharField(_('name'), max_length=100)
    series = models.ForeignKey(Series, verbose_name=_('series'), related_name='models')
    thumb_off = models.ImageField(_('thumb off'), upload_to=off_upload_path)
    thumb_on = models.ImageField(_('thumb on'), upload_to=on_upload_path)
    description = models.TextField(_('description'))

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100)
    model = models.ForeignKey(Model, verbose_name=_('model'), related_name='products')
    material = models.CharField(_('material'), max_length=100)
    specs = models.CharField(_('specs'), max_length=100)

    def __unicode__(self):
        return self.name
    

class ProductImage(models.Model):
    def upload_path(self, filename):
        return 'products/%s/%s' % (self.model.name, filename)

    name = models.CharField(_('name'), max_length=100)
    model = models.ForeignKey(Model, verbose_name=_('model'), related_name='images')
    image = models.ImageField(_('image'), upload_to=upload_path)

    def __unicode__(self):
        return self.name
        

