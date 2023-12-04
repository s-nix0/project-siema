from django.contrib import admin
from .models import Analytic


class AnalyticAdmin(admin.ModelAdmin):
    list_display = ('formatted_timestamp', 'request_method', 'page_url', 'status_code', 'ip_address', 'user_agent')
    list_filter = ('request_method', 'status_code')  # Add more fields as needed

    def formatted_timestamp(self, obj):
        return obj.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    formatted_timestamp.short_description = 'Timestamp'


admin.site.register(Analytic, AnalyticAdmin)
