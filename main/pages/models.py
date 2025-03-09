from django.db import models
from django.utils.html import mark_safe
# Create your models here.
from django.utils.functional import lazy
from django.utils.translation import gettext_lazy as _
from PIL import Image

class VerboseName(str):
    def __init__(self, func):
        self.func = func

    def decode(self, encoding, erros):
        return self.func().decode(encoding, erros)


class project(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_default_image(self):
        return self.photos.filter(is_default=True)

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"


class project_photo(models.Model):
    project = models.ForeignKey(
        project, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    is_default = models.BooleanField()

    class Meta:
        verbose_name = "Proje Fotoğrafı"
        verbose_name_plural = "Proje Fotoğrafları"

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        if img.height > 1280 or img.width > 720:
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.image.path)



class message(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, default='', blank=True)
    subject = models.CharField(max_length=30)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = lazy(
            lambda: _('Articles ({})').format(message.objects.filter(is_read=False).count()), str)()

    def __str__(self) -> str:
        return self.name + " " + self.subject



class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    subtitle = models.CharField(max_length=300, blank=True, verbose_name="Alt Başlık")
    header_image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name="Başlık Resmi")
    main_content = models.TextField(verbose_name="Ana İçerik")
    mission_statement = models.TextField(blank=True, verbose_name="Misyon Bildirimi")
    team_description = models.TextField(blank=True, verbose_name="Ekip Açıklaması")
    address = models.TextField(blank=True, verbose_name="Adres")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="E-posta")
    working_hours = models.CharField(max_length=200, blank=True, verbose_name="Çalışma Saatleri")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncelleme")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hakkımızda Sayfası"
        verbose_name_plural = "Hakkımızda Sayfası"






class Main(models.Model):
    # Hero Section
    hero_title = models.CharField(max_length=200, verbose_name="Hero Başlık")
    hero_subtitle = models.CharField(max_length=300, verbose_name="Hero Alt Başlık")
    hero_background_image = models.ImageField(upload_to='main/', verbose_name="Hero Arkaplan Resmi")
    hero_video_url = models.URLField(verbose_name="Hero Video URL")

    # Section 1
    sec1_title = models.CharField(max_length=200, verbose_name="Bölüm 1 Başlık")
    sec1_content = models.TextField(verbose_name="Bölüm 1 İçerik")
    sec1_image = models.ImageField(upload_to='main/', verbose_name="Bölüm 1 Resim")

    # Section 2
    sec2_title = models.CharField(max_length=200, verbose_name="Bölüm 2 Başlık")
    sec2_content = models.TextField(verbose_name="Bölüm 2 İçerik")
    sec2_image = models.ImageField(upload_to='main/', verbose_name="Bölüm 2 Resim")

    # Section 3 (Services)
    sec3_title = models.CharField(max_length=200, verbose_name="Bölüm 3 Başlık")
    sec3_content = models.TextField(verbose_name="Bölüm 3 İçerik")

    # Accordion Items
    accordion_interior_title = models.CharField(max_length=200, verbose_name="Interior Design Başlık")
    accordion_interior_content = models.TextField(verbose_name="Interior Design İçerik")
    accordion_interior_image = models.ImageField(upload_to='main/', verbose_name="Interior Design Resim")

    accordion_landscape_title = models.CharField(max_length=200, verbose_name="Landscape Design Başlık")
    accordion_landscape_content = models.TextField(verbose_name="Landscape Design İçerik")
    accordion_landscape_image = models.ImageField(upload_to='main/', verbose_name="Landscape Design Resim")

    accordion_engineering_title = models.CharField(max_length=200, verbose_name="Engineering Plan Başlık")
    accordion_engineering_content = models.TextField(verbose_name="Engineering Plan İçerik")
    accordion_engineering_image = models.ImageField(upload_to='main/', verbose_name="Engineering Plan Resim")

    accordion_architecture_title = models.CharField(max_length=200, verbose_name="Architecture Design Başlık")
    accordion_architecture_content = models.TextField(verbose_name="Architecture Design İçerik")
    accordion_architecture_image = models.ImageField(upload_to='main/', verbose_name="Architecture Design Resim")

    def __str__(self):
        return self.hero_title

    class Meta:
        verbose_name = "Ana Sayfa İçeriği"
        verbose_name_plural = "Ana Sayfa İçeriği"