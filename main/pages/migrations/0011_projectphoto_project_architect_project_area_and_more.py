# Generated by Django 4.2.2 on 2025-03-09 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_photos/', verbose_name='Fotoğraf')),
                ('is_default', models.BooleanField(default=False, verbose_name='Varsayılan Fotoğraf')),
                ('caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='Fotoğraf Açıklaması')),
            ],
            options={
                'verbose_name': 'Proje Fotoğrafı',
                'verbose_name_plural': 'Proje Fotoğrafları',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='architect',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mimar'),
        ),
        migrations.AddField(
            model_name='project',
            name='area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Proje Alanı (m²)'),
        ),
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Proje Bütçesi'),
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Müşteri'),
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Bitiş Tarihi'),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Proje Lokasyonu'),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Başlangıç Tarihi'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('planning', 'Planlama Aşamasında'), ('ongoing', 'Devam Ediyor'), ('completed', 'Tamamlandı')], default='planning', max_length=50, verbose_name='Proje Durumu'),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Proje Yılı'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Proje Açıklaması'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Proje Adı'),
        ),
        migrations.DeleteModel(
            name='project_photo',
        ),
        migrations.AddField(
            model_name='projectphoto',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='pages.project', verbose_name='Proje'),
        ),
    ]
