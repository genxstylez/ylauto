from django.contrib import admin
from django.conf import settings
from product.models import Category, Make, Series, Model, Product, ProductImage
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

class CategoryAdmin(TranslationAdmin):
    class Media:
        js = (
            '%sgrappelli/tinymce/jscripts/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%sjs/tinymce_setup.js' % settings.STATIC_URL,
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/jquery-ui.min.js',
            'grappelli_modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
             'screen': ('grappelli_modeltranslation/css/tabbed_translation_fields.css',)
        }

class MakeAdmin(TranslationAdmin):
     class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/jquery-ui.min.js',
            'grappelli_modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('grappelli_modeltranslation/css/tabbed_translation_fields.css',)
        }


class SeriesAdmin(TranslationAdmin):
     class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/jquery-ui.min.js',
            'grappelli_modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('grappelli_modeltranslation/css/tabbed_translation_fields.css',)
        }

class ProductAdmin(TranslationAdmin):
     class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/jquery-ui.min.js',
            'grappelli_modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('grappelli_modeltranslation/css/tabbed_translation_fields.css',)
        }


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ModelAdmin(TranslationAdmin):
    inlines = [ ProductImageInline, ]
    class Media:
        js = (
            '%sgrappelli/tinymce/jscripts/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%sjs/tinymce_setup.js' % settings.STATIC_URL,
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/jquery-ui.min.js',
            'grappelli_modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('grappelli_modeltranslation/css/tabbed_translation_fields.css',)
        }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Make, MakeAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Product, ProductAdmin)
