# Generated by Django 3.0.2 on 2020-12-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201208_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uz',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Название'),
        ),
    ]
