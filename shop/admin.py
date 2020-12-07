from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('id', 'name', 'category', 'price', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')

class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class NewsAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class ShopsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Shops, ShopsAdmin)