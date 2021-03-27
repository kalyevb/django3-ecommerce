# Generated by Django 3.0.8 on 2021-03-26 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20210317_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=1, upload_to='', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=1, upload_to='', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
