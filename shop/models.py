from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название продукта')
    slug = models.SlugField(max_length=30, verbose_name='Url', unique=True, null=True)
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    price = models.IntegerField(default=0, verbose_name='Цена(сум)')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=30, verbose_name='Url', unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
    


class About(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовка')
    slug = models.SlugField(max_length=30, verbose_name='Url', unique=True, null=True)
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("about", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название новости')
    slug = models.SlugField(max_length=30, verbose_name='Url', unique=True, null=True)
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Shops(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название магазина')
    slug = models.SlugField(max_length=30, verbose_name='Url', unique=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    slogan = models.CharField(max_length=30, verbose_name='Слоган')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        
