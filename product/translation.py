from modeltranslation.translator import translator, TranslationOptions
from product.models import Category, Make, Series, Model, Product, ProductImage

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


class MakeTranslationOptions(TranslationOptions):
    fields = ('name', )


class SeriesTranslationOptions(TranslationOptions):
    fields = ('name', )


class ModelTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'material', 'specs', )


class ProductImageTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)
translator.register(Make, MakeTranslationOptions)
translator.register(Series, SeriesTranslationOptions)
translator.register(Model, ModelTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(ProductImage, ProductImageTranslationOptions)

