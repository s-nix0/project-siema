from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve
from django.contrib.auth.decorators import login_required
from .views import HomeView, DashboardView, SearchView, ArticleListVew, ArticleDetailView, MaterialListVew, \
    MaterialDetailView, ComicListVew, ComicDetailView, QuizListVew, QuizDetailView, ToS, PrivacyPolicy, AboutView, GuideView
from .sitemainpath import SitemapView, RobotsView, GoogleVerifyView

urlpatterns = [
    path('googleea42fa73b7b371df.html', GoogleVerifyView.as_view(), name='google_verify'),
    path('sitemap.xml', SitemapView.as_view(), name='sitemap'),
    path('robots.txt', RobotsView.as_view(), name='robots'),
    path('', HomeView.as_view(), name="home"),
    path('tentang/', AboutView.as_view(), name="about"),
    path('panduan/', GuideView.as_view(), name="guide"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('cari/', SearchView.as_view(), name='search'),
    # path('artikel/', ArticleListVew.as_view(), name='article-list'),
    path('artikel/', RedirectView.as_view(url='dashboard', permanent=True), name='article-list'),
    path('materi/', MaterialListVew.as_view(), name='material-list'),
    path('komik/', ComicListVew.as_view(), name='comic-list'),
    path('kuis/', QuizListVew.as_view(), name='quiz-list'),
    # path('artikel/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('materi/<int:level>', login_required(MaterialDetailView.as_view()), name='material-detail'),
    path('komik/<int:level>', login_required(ComicDetailView.as_view()), name='comic-detail'),
    path('kuis/<int:level>', login_required(QuizDetailView.as_view()), name='quiz-detail'),
    path('ketentuan-layanan/', ToS.as_view(), name='tos'),
    path('kebijakan-privasi/', PrivacyPolicy.as_view(), name='privacy-policy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
