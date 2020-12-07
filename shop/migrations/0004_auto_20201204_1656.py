# Generated by Django 3.0.2 on 2020-12-04 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201203_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['title'], 'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='about',
            name='slug',
            field=models.SlugField(max_length=30, null=True, unique=True, verbose_name='Url'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=30, null=True, unique=True, verbose_name='Url'),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=30, null=True, unique=True, verbose_name='Url'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=30, null=True, unique=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена(сум)'),
        ),
    ]