from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from pages.models import Project  # BlogPost referansını kaldırıyorum

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'services', 'contact']

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Project.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

# BlogSitemap sınıfını kaldırıyorum çünkü BlogPost modeli mevcut değil



