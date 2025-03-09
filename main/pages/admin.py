from django.contrib import admin
from .models import project, project_photo, message, Main, About
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






from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # Admin panelinde görüntülenecek alanlar
    list_display = ('title', 'subtitle', 'updated_at')
    
    # Arama çubuğu ekleme
    search_fields = ('title', 'subtitle', 'main_content')
    
    # Filtreleme seçenekleri
    list_filter = ('updated_at',)
    
    # Alanları gruplayarak gösterme
    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('title', 'subtitle', 'header_image', 'main_content')
        }),
        ('Misyon ve Ekip', {
            'fields': ('mission_statement', 'team_description')
        }),
        ('İletişim Bilgileri', {
            'fields': ('address', 'phone', 'email', 'working_hours')
        }),
    )
    
    # Otomatik olarak güncellenen alanları gizleme
    readonly_fields = ('updated_at',)
    
    # Admin panelinde kayıtları tarihe göre sıralama
    date_hierarchy = 'updated_at'









@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('hero_title', 'hero_subtitle')
    search_fields = ('hero_title', 'hero_subtitle')
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_background_image', 'hero_video_url')
        }),
        ('Section 1', {
            'fields': ('sec1_title', 'sec1_content', 'sec1_image')
        }),
        ('Section 2', {
            'fields': ('sec2_title', 'sec2_content', 'sec2_image')
        }),
        ('Section 3 (Services)', {
            'fields': ('sec3_title', 'sec3_content')
        }),
        ('Accordion Items', {
            'fields': (
                'accordion_interior_title', 'accordion_interior_content', 'accordion_interior_image',
                'accordion_landscape_title', 'accordion_landscape_content', 'accordion_landscape_image',
                'accordion_engineering_title', 'accordion_engineering_content', 'accordion_engineering_image',
                'accordion_architecture_title', 'accordion_architecture_content', 'accordion_architecture_image'
            )
        }),
    )


admin.site.register(project, projectAdmin)
admin.site.register(message, messageAdmin)
