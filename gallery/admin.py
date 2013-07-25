from django.contrib import admin
from gallery.models import Gallery, GalleryItem
from django.conf import settings
from modeltranslation.admin import TranslationAdmin

class GalleryItemInline(admin.TabularInline):
    model = GalleryItem
    extra = 3

class GalleryAdmin(TranslationAdmin):
    inlines = [ GalleryItemInline, ]
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

admin.site.register(Gallery, GalleryAdmin)
