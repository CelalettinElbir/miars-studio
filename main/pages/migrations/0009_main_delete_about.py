# Generated by Django 4.2.2 on 2025-03-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_about_alter_message_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.CharField(max_length=200, verbose_name='Hero Başlık')),
                ('hero_subtitle', models.CharField(max_length=300, verbose_name='Hero Alt Başlık')),
                ('hero_background_image', models.ImageField(upload_to='main/', verbose_name='Hero Arkaplan Resmi')),
                ('hero_video_url', models.URLField(verbose_name='Hero Video URL')),
                ('sec1_title', models.CharField(max_length=200, verbose_name='Bölüm 1 Başlık')),
                ('sec1_content', models.TextField(verbose_name='Bölüm 1 İçerik')),
                ('sec1_image', models.ImageField(upload_to='main/', verbose_name='Bölüm 1 Resim')),
                ('sec2_title', models.CharField(max_length=200, verbose_name='Bölüm 2 Başlık')),
                ('sec2_content', models.TextField(verbose_name='Bölüm 2 İçerik')),
                ('sec2_image', models.ImageField(upload_to='main/', verbose_name='Bölüm 2 Resim')),
                ('sec3_title', models.CharField(max_length=200, verbose_name='Bölüm 3 Başlık')),
                ('sec3_content', models.TextField(verbose_name='Bölüm 3 İçerik')),
                ('accordion_interior_title', models.CharField(max_length=200, verbose_name='Interior Design Başlık')),
                ('accordion_interior_content', models.TextField(verbose_name='Interior Design İçerik')),
                ('accordion_interior_image', models.ImageField(upload_to='main/', verbose_name='Interior Design Resim')),
                ('accordion_landscape_title', models.CharField(max_length=200, verbose_name='Landscape Design Başlık')),
                ('accordion_landscape_content', models.TextField(verbose_name='Landscape Design İçerik')),
                ('accordion_landscape_image', models.ImageField(upload_to='main/', verbose_name='Landscape Design Resim')),
                ('accordion_engineering_title', models.CharField(max_length=200, verbose_name='Engineering Plan Başlık')),
                ('accordion_engineering_content', models.TextField(verbose_name='Engineering Plan İçerik')),
                ('accordion_engineering_image', models.ImageField(upload_to='main/', verbose_name='Engineering Plan Resim')),
                ('accordion_architecture_title', models.CharField(max_length=200, verbose_name='Architecture Design Başlık')),
                ('accordion_architecture_content', models.TextField(verbose_name='Architecture Design İçerik')),
                ('accordion_architecture_image', models.ImageField(upload_to='main/', verbose_name='Architecture Design Resim')),
            ],
            options={
                'verbose_name': 'Ana Sayfa İçeriği',
                'verbose_name_plural': 'Ana Sayfa İçeriği',
            },
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
