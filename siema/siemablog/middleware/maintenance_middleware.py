from django.http import HttpResponseServerError
from django.template import loader
from django.conf import settings
from django.utils import timezone
from datetime import datetime


class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        maintenance_mode, end_time = self.get_maintenance_info()

        if maintenance_mode and not request.path_info.startswith('/admin/'):
            if self.is_within_maintenance_window(end_time):
                remaining_time = self.calculate_remaining_time(end_time)
                return self.render_maintenance_page(end_time, remaining_time)

        response = self.get_response(request)
        return response

    def render_maintenance_page(self, end_time, remaining_time):
        template = loader.get_template('maintenance.html')
        context = {'end_time': end_time, 'remaining_time': remaining_time}
        return HttpResponseServerError(template.render(context))

    def calculate_remaining_time(self, end_time):
        if end_time:
            remaining_time = end_time - timezone.now()
            return int(remaining_time.total_seconds())  # Convert timedelta to seconds
        return None

    # def format_timedelta(self, delta):
    #     days, seconds = delta.days, delta.seconds
    #     hours = seconds // 3600
    #     minutes = (seconds % 3600) // 60
    #     seconds = seconds % 60
    #     return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

    def is_within_maintenance_window(self, end_time):
        if end_time:
            now = timezone.now()
            return now <= end_time
        return False

    def get_maintenance_info(self):
        maintenance_mode = getattr(settings, 'MAINTENANCE_MODE', False)
        end_time = getattr(settings, 'MAINTENANCE_END_TIME', None)

        if end_time:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

        return maintenance_mode, end_time
