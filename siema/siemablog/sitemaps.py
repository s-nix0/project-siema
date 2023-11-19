# views.py
from django.views.generic import TemplateView


class SitemapView(TemplateView):
    template_name = 'sitemap.xml'

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response['Content-Type'] = 'application/xml'
        return response
