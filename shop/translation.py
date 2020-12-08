from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category, About, Shops

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'content', 'category')



@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Shops)
class ShopsTranslationOptions(TranslationOptions):
    fields = ('title', 'slogan')

