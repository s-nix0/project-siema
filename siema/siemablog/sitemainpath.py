from django.views.generic import TemplateView


class GoogleVerifyView(TemplateView):
    template_name = 'googleea42fa73b7b371df.html'

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response['Content-Type'] = 'text/html'
        return response


class SitemapView(TemplateView):
    template_name = 'sitemap.xml'

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response['Content-Type'] = 'application/xml'
        return response


class RobotsView(TemplateView):
    template_name = 'robots.txt'

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response['Content-Type'] = 'text/plain'
        return response
