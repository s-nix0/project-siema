from django.urls import path
# from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import HomeView, ArtikelListVew, ArtikelDetailView, MateriListVew, MateriDetailView, KomikListVew, \
    KomikDetailView, KuisListVew, KuisDetailView

urlpatterns = [
                  # path('', views.home, name="home"),
                  path('', HomeView.as_view(), name="home"),
                  path('artikel/', ArtikelListVew.as_view(), name='artikel-daftar'),
                  path('materi/', MateriListVew.as_view(), name='materi-daftar'),
                  path('komik/', KomikListVew.as_view(), name='komik-daftar'),
                  path('kuis/', KuisListVew.as_view(), name='kuis-daftar'),
                  path('artikel/<int:pk>', ArtikelDetailView.as_view(), name='artikel-detail'),
                  path('materi/<int:level>', login_required(MateriDetailView.as_view()), name='materi-detail'),
                  path('komik/<int:level', login_required(KomikDetailView.as_view()), name='komik-detail'),
                  path('kuis/<int:level>', login_required(KuisDetailView.as_view()), name='kuis-detail'),
                  # path('update-user-activity/', update_user_activity, name='update-user-activity'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
