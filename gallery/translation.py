from modeltranslation.translator import translator, TranslationOptions
from gallery.models import Gallery

class GalleryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Gallery, GalleryTranslationOptions)
