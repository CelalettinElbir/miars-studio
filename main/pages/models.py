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
