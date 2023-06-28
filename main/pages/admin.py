from django.contrib import admin
from .models import project, project_photo, message
from django.utils.html import format_html
from django.forms import inlineformset_factory
from django.db import models
from django import forms
from PIL import Image
# from .forms import ProjectPhotosForm
# Register your models here.
def resize_image(image_path, target_width):
    image = Image.open(image_path)
    width, height = image.size

    # Belirli bir genişlik (target_width) üzerinden yükseklik hesaplanır
    target_height = int((height / width) * target_width)

    resized_image = image.resize((target_width, target_height), Image.ANTIALIAS)
    resized_image.save(image_path)

class messageAdmin(admin.ModelAdmin):
    model = message

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        obj.is_read = True  # veya False olarak güncelleyin
        obj.save()
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)


class ProjectPhotosInline(admin.StackedInline):
    model = project_photo


class projectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "show_photos")

    inlines = [
        ProjectPhotosInline,
    ]
    class Meta:
        model = project

    def show_photos(self, obj):
        result = ""

        for i in obj.photos.all():
            result += f"<img src='{  i.image.url }'  width='100px' height='100px' style = 'margin:3px;'/>"
        return format_html(result)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image_path = self.image.path
        resize_image(image_path, 1200)  


admin.site.register(project, projectAdmin)
admin.site.register(message, messageAdmin)
