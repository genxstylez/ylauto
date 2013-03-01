from django.contrib import admin
from django.conf import settings
from general.models import About, ImageSlide
from modeltranslation.admin import TranslationAdmin


class AboutAdmin(TranslationAdmin):
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


admin.site.register(About, AboutAdmin)
admin.site.register(ImageSlide)
