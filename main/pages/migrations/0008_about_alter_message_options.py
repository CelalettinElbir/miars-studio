# Generated by Django 4.2.2 on 2025-03-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_project_options_alter_project_photo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('subtitle', models.CharField(blank=True, max_length=300, verbose_name='Alt Başlık')),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Başlık Resmi')),
                ('main_content', models.TextField(verbose_name='Ana İçerik')),
                ('mission_statement', models.TextField(blank=True, verbose_name='Misyon Bildirimi')),
                ('team_description', models.TextField(blank=True, verbose_name='Ekip Açıklaması')),
                ('address', models.TextField(blank=True, verbose_name='Adres')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Telefon')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-posta')),
                ('working_hours', models.CharField(blank=True, max_length=200, verbose_name='Çalışma Saatleri')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme')),
            ],
            options={
                'verbose_name': 'Hakkımızda Sayfası',
                'verbose_name_plural': 'Hakkımızda Sayfası',
            },
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Mesaj', 'verbose_name_plural': 'Articles (0)'},
        ),
    ]
