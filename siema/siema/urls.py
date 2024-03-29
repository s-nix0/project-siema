"""
URL configuration for siema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = 'SIEMA Administration'  # default: "Django Administration"
admin.site.index_title = 'Site Administration'  # default: "Site administration"
admin.site.site_title = 'SIEMA Site Admin'  # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('siemablog.urls')),
    # path('akun/', include('django.contrib.auth.urls')),
    path('akun/', include('akun.urls')),
    path('kontak/', include('feedback.urls')),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'siemablog.views.handling_404'
