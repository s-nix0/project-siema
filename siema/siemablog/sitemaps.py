# views.py
from django.views.generic import TemplateView


class SitemapView(TemplateView):
    template_name = 'sitemap.xml'

    def get_context_data(self, **kwargs):
        # Define your URLs here or retrieve them from your database
        urls = [
            {"loc": "/", "lastmod": "2023-01-01", "changefreq": "monthly", "priority": "1.0"},
            {"loc": "/dashboard", "lastmod": "2023-01-02", "changefreq": "monthly", "priority": "0.8"},
            {"loc": "/kontak", "lastmod": "2023-01-03", "changefreq": "monthly", "priority": "0.8"},
            {"loc": "/akun/login", "lastmod": "2023-01-04", "changefreq": "monthly", "priority": "0.8"},
        ]
        return {'urls': urls}
