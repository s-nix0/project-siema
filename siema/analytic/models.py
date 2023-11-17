# models.py
from django.db import models


class Analytic(models.Model):
    page_url = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    referrer = models.URLField(null=True, blank=True)
    device_type = models.TextField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    request_method = models.CharField(null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_method} | {self.page_url} | {self.status_code} - {self.ip_address} - {self.user_agent}"
