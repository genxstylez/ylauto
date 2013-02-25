from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    name = models.CharField(_('name'), max_length=100)


class Make(models.Model):
    name = models.CharField(_('name'), max_length=100)
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='makes')


class Series(models.Model):
    name = models.CharField(_('name'), max_length=100)
    make = models.ForeignKey(Make, verbose_name=_('make'), related_name='series')


class Model(models.Model):
    def upload_path(self):
        return 'products/%s/thumb' % self.name
    name = models.CharField(_('name'), max_length=100)
    series = models.ForeignKey(Series, verbose_name=_('series'), related_name='models')
    thumb = models.ImageField(_('thumb'), upload_to=upload_path)
    description = models.TextField(_('description'))


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100)
    model = models.ForeignKey(Model, verbose_name=_('model'), related_name='products')
    material = models.CharField(_('material'), max_length=100)
    specs = models.CharField(_('specs'), max_length=100)
    

class ProductImage(models.Model):
    def upload_path(self):
        return 'products/%s/images' % self.model.name

    name = models.CharField(_('name'), max_length=100)
    model = models.ForeignKey(Model, verbose_name=_('model'), related_name='images')
    image = models.ImageField(_('image'), upload_to=upload_path)
        
