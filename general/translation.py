from modeltranslation.translator import translator, TranslationOptions
from general.models import About

class AboutTranslationOptions(TranslationOptions):
    fields = ('content',)

translator.register(About, AboutTranslationOptions)
