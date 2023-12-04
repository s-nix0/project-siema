from .models import Analytic


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Track analytics for all URLs
        Analytic.objects.create(
            page_url=request.path_info,
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT'),
            referrer=request.META.get('HTTP_REFERER'),
            device_type=request.META.get('HTTP_USER_AGENT'),
            request_method=request.method,
            status_code=response.status_code,
            post_data=request.POST.dict() if request.method == 'POST' else None
        )

        return response
