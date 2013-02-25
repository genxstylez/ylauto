from django.contrib import admin
from product.models import Category, Make, Series, Model, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ModelAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]
    class Media:
        js = [
            '/asset/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/asset/js/tinymce_setup.js',
        ]

admin.site.register(Category)
admin.site.register(Make)
admin.site.register(Series)
admin.site.register(Model, ModelAdmin)
admin.site.register(Product)
